Welcome to my writeup series about the Hacker101 CTF by Hackerone! This challenge is called “A little something to get you started” and it is in the trivial category.

Upon launching this challenge, we are met with the text “Welcome to level 0. Enjoy your stay.”

![Image 1](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*YFPnNl41MyRx53if153thw.png)

Checking the page source reveals some CSS that uses a background image called background.png.

```<style> body { background-image: url(“background.png”); } </style>```

We can manually append /background.png to the URL, which reveals the flag.

![Image 2](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*j78sG9rMVnVWdeR7pG4-0Q.png)
