In the Micro-CMS V2 CTF by Hackerone, we are given the following hints for the first flag:

- Regular users can only see public pages
- Getting admin access might require a more perfect union
- This immediately made me think about SQL Injection UNION attacks, which you can learn about here.

I began by checking for some basic SQL Injection vulnerabilities with a ```‘``` and ```admin’```.

![Image 1](https://miro.medium.com/v2/resize:fit:640/format:webp/1*_6GWah2C6DvE-OztGnTJtw.png)

These returned errors, but did not provide any useful information.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*WeFgg9-MUkzV1kGxF2REJg.png)

I considered opening Burpsuite Intruder and attempting to brute force the username/password combination, but assumed it would be a difficult combination because of the union hint.

I tried a few different payloads, but struggled to blindly guess what the name of the table name was. Eventually, I did some cheating and checked online to see if I could learn the name of the table. I found a writeup saying that the table name was ```admins```.

The final payload I used was:

```' UNION SELECT 'pass' AS password FROM admins WHERE '1' = '1```

And for the password field:

```pass```

![Image 1](https://miro.medium.com/v2/resize:fit:640/format:webp/1*g3l70O6ae8WNMAEDoN-pvA.png)

Submitting that gave me message saying that I was logged in.

![Image 1](https://miro.medium.com/v2/resize:fit:640/format:webp/1*lGEwkNgZj8jZ0dVW2_z3wA.png)

Clicking on the link to the Private Page displayed the flag.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*vU_B9UgFj-voMGM1jKeXvg.png)

The hint for the next flag said: What actions could you perform as a regular user on the last level, which you can’t now?

The “changelog” for page 1 also said: “This version fixed the multitude of security flaws and general functionality bugs that plagued v1. Additionally, we added user authentication; we’re still not sure why we didn’t think about that the first time, but hindsight is 20/20. By default, users need to be an admin to add or edit pages now.”

I used Burpsuite to modify requests and was unable to find an answer that way. Later, I learned that you can send different HTTP request methods using Curl from the command line using the “-X POST” argument. My final command was:

```curl -X POST https://7b44997630caaec756ff4da81538e9c9.ctf.hacker101.com/page/edit/1```

This immediately gave the second flag.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*F6Ewk16HVoFad3gF8qOGwA.png)

The hint for the last flag was: Credentials are secret, flags are secret. Coincidence? I ended up using Burpsuite for this flag as well. My plan was to brute force the username and password, hoping it wasn’t too complex. I recalled from doing this in the past that the username and password were first names. In the past, I had used [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt), but that took quite a while.

This time, I used a [wordlist](https://raw.githubusercontent.com/ternera/hacker101-ctf/main/names.txt) with only first names in hopes that the challenge was still configured that way. I used Burpsuite’s intercept proxy and then sent the request to the intruder.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*Pkaaf2gPQt_8h7Uq8K0U2Q.png)

After configuring positions and uploading my wordlist, I began the attack and found that the username was “betsy”, seeing it had a different length than the rest of the responses.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*DC18q3DTBfvqYoUw5SDqEQ.png)

Trying the username “betsy” with a random password returned an “Invalid password” error, so that showed me that I was on the correct track.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*kX_K-9Te1BzUKxzoFEX6Wg.png)

After running the attack for a few more minutes, the password “teresa” also returned a different length.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*CE85jLkCq_xYNIVMMpmCvg.png)

Using the username “betsy” and password “teresa” authenticated me and immediately returned the flag.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*tBh2F2DedcKKlxlvUp2wXg.png)

That means this challenge has been completely solved. Be sure to view some of my other Hacker101 CTF writeups!
