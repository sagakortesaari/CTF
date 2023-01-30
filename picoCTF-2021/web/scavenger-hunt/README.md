# Scavenger Hunt 

There is some interesting information hidden around this site http://mercury.picoctf.net:39698/. Can you find it?

## Solution 

Upon inspecting the HTML on the frontpage, we can see a part of the flag `<!-- Here's the first part of the flag: picoCTF{t -->` so I guess we'll actually have to do what the name suggests, a scavenger hunt. 

Part 2 of the flag can be found in the CSS file mycss.css. `Part 2: h4ts_4_l0`

myjs.js contains `How can I keep Google from indexing my website?`, and the answer is obviously /robots.txt, which reveals part 3, `Part 3: t_0f_pl4c`.

/robots.txt also contains `"# I think this is an apache server... can you Access the next flag?"`, so /.htaccess reveals part 4, `Part 4: 3s_2_lO0k`.

/.htaccess also contains `"I love making websites on my Mac, I can Store a lot of information there."` which in turn suggests those annoying .DS_Store files that floods my mac 24/7. 

/.DS_Store reveals the final part `Congrats! You completed the scavenger hunt. Part 5: _fa04427c}`. :)

