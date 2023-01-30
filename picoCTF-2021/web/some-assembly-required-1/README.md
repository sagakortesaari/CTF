# Some Assembly Required 1

http://mercury.picoctf.net:36152/index.html

## Solution

We're met with a form with the text "enter flag". The submit button of the form calls the `onButtonPress()` function, which one can see in the corresponding js-file. At first, I started to deep-dive into the weird js-file, but upon closer inspection I realized there is a path inside the array at the top `./JIFxzHyW8W`. Visiting the path downloads a file, where we can find the flag at the bottom. 

