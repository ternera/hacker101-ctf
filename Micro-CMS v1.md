Upon launching this challenge in the CTF, we are met with three links, labeled: Testing, Markdown Test, and Create a new page.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*RlwQNGGgZl4ELTaWIbzUFg.png)

The first hint suggests to try creating a new page. The new page creation page says that [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is supported, but scripts are not.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*dwLIdQIU7jYQFDx2lE4j0g.png)

After creating a new page, I noticed something interesting. It was assigned the number 12. I wondered if I could modify the URL and possibly find some information in pages with other numbers.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*f1kLgtJaKGKKb0gBNofXMQ.png)

Page 7 returned a Forbidden error. That’s interesting.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*D-MkAHr9-26Wp9MzHWHTtw.png)

It looked like the only pages I could access were 1, 2, and 12. 1 and 2 had already been created and 12 was the page that I created. After taking a closer look at the existing pages, I noticed there was an edit button on these pages. I opened the editing page for page 2.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*8JOfarDKJMHr3Wv3Q1HRTw.png)

Similar to the “A little something to get you started” challenge, I found that you could change the page number to edit the protected page 7.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*irYtwuF4jsCWqO41Flz3zw.png)

This revealed the first flag from this challenge. For the second flag, the only hint given said to tamper with every input. After playing with the text box, I directed my attention back to the URL. Originally, I tried appending ‘1=1 to the URL, but found that simply adding one ‘ at the end of the URL would reveal the second flag.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*VQlexFPuqGsBz9WlqDwLIw.png)

The next flag was found before some others, but I am putting it here to keep things in order. I wanted to try some [Markdown XSS](https://github.com/cujanovic/Markdown-XSS-Payloads/blob/master/Markdown-XSS-Payloads.txt) because I noticed that the message “[Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is supported, but scripts are not” was shown when creating a new page. Unfortunately, I looked over something important here. The body of the text area says it doesn’t support scripts, but the title does not mention anything about it. I found this out accidentally after using the following from the [Markdown XSS](https://github.com/cujanovic/Markdown-XSS-Payloads/blob/master/Markdown-XSS-Payloads.txt) repo:

```<javascript:prompt(document.cookie)>```

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*NH2h4EGvvawr8rKbusG9BQ.png)

After saving, this is what I saw on the page:

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*0vc24PUNuDr2r5ZwdJJxAg.png)

Clicking the “Go Home” link returned a popup with the flag.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*Awn9MhEbAntq6LT9dGAZFQ.png)

The hint for the final flag says that “Scripts are great, but what other options do you have?” This made me circle back around to my original thought of using some markdown XSS. This didn’t get me anywhere, so I did a quick Google search for “how to add xss to other tags” to see if I could find any articles that would shed some light on the matter. I found this [helpful post](https://security.stackexchange.com/a/24910) on Stack Overflow that shows how to modify a div tag to execute a script. I copied and pasted their div tag into the body of the text box.

```<div onmouseover="alert(1)" style="position:fixed;left:0;top:0;width:9999px;height:9999px;"></div>```

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*Kly-1HAfVWPBsw3pRybkKQ.png)

Immediately after creating the page, I was met with a popup with a value of 1.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*IxqY2nrKzLhcK4kV2biTPw.png)

I didn’t find the flag on the homepage like the previous flag, but instead it was hidden in the source code of the page I created.

![Image 1](https://miro.medium.com/v2/resize:fit:720/format:webp/1*nLc_plyFrACwoPz4AaiMKQ.png)

That wraps up this CTF challenge, see you in the next one!