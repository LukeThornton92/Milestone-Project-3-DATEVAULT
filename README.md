# **The Date Vault**

This website is designed to help couples plan date nights by allowing them to store and randomly retrieve date ideas. Couples can input their unique date ideas with specific compulsory fields. Later, they can filter and request a random idea that suits their preferences from the database they have built over time.

You can access the live site via the following URL. - https://github.com/LukeThornton92/Milestone-Project-3-DATEVAULT

## **Site Overview**

<img src="" alt="">

## Table of Contents:

1. [**Site Overview**](#site-overview)
2. [**Planning stage**](#planning-stage)
   - [**_Target Audiences_**](#target-audiences)
   - [**_User Stories_**](#user-stories)
   - [**_Site Aims_**](#site-aims)
   - [**_How Will This Be Achieved_**](#how-will-this-be-achieved)
   - [**_Research_**](#research)
   - [**_Wireframes_**](#wireframes)
3. [**Building Stage**](#building-stage)
   - [**_Colour Scheme_**](#colour-scheme)
   - [**_Typography_**](#typography)
4. [**Features**](#features)
   - [**_Home Page_**](#home-page)
   - [**_404_**](#404)
5. [**Future Enhancements**](#future-enhancements)
6. [**Testing**](#testing)
   - [**_Validator Testing_**](#validator-testing)
7. [**Deployment**](#deployment)
8. [**Credits**](#credits)
   - [**_Honourable Mentions_**](#honourable-mentions)
   - [**_General Reference_**](#general-refrence)
   - [**_Content_**](#content)
   - [**_Media_**](#media)

---

## **Planning Stage**

### **Target Audiences:**

- Couples of all ages looking for fresh and fun date ideas to strengthen their relationship.
- Busy partners who want a quick and easy way to generate personalized date plans without spending hours planning.
- Long-term couples seeking new and spontaneous experiences to break routine and keep things exciting.
- Tech-savvy or beginner users who appreciate a user-friendly platform for managing and discovering date ideas.

### **User Stories:**

- As a user, I want to easily input date ideas with specific details so that I can save them for future use.
- As a user, I want to filter date ideas by budget, location, and activity type so I can find the perfect idea for my needs.
- As a user, I want to receive a randomized date idea from my filtered results so I can experience something new and exciting.
- As a user, I want to edit or update my saved date ideas so I can keep my list relevant and up-to-date.
- As a user, I want the interface to be simple and intuitive so I can quickly navigate the site without confusion.
- As a user, I want my data to be stored securely so that I can trust my personal information is safe.

### **Site Aims:**

- To create an accessible and intuitive platform for couples to share and retrieve personalized date ideas.
- To ensure the system offers a variety of filters to allow for a personalized experience when retrieving date ideas.
- To provide randomised suggestions based on user preferences to keep the experience fun and spontaneous.
- To encourage couples to build a rich database of date ideas over time.
- To have a professional look and feel suitable for adults.

### **How Will This Be Achieved:**

My project will ensure the above aims and features are accomplished by successfully achieving the following targets.

- **Database Integration:** Set up a database to store date ideas with compulsory fields (e.g., activity type, cost, duration).
- **Date Input Form:** Develop a form to capture date ideas with validation for compulsory fields.
- **Search and Filter Functionality:** Implement a filtering system based on user preferences such as budget, activity type, and location.
- **Random Date Selector:** Create functionality that selects a random date idea from the filtered search results.
- **User Interface Design:** Focus on building an intuitive, attractive interface for easy navigation and interaction.
- **Security:** Implement basic security features to protect user input and data.

### **Nice To Have's:**

The following items will be nice to have, I will aim to get them into the website in time but these will not be the initial focus.

- Ability to email partners to sign up.
- Google calendar invite for desired dates.

### **Research:**

1. https://mattbateman.net/fun/date-idea-generator/

#### Likes

> - First site found when searched.
> - Has filters.

#### Dislikes

> - Very basic.
> - Cant personalize.
> - Poor design.
> - Can't save any ideas.

---

2. https://thedateidea.com/

#### Likes

> - Modern design.
> - Has blog posts around certain types of dates/date ideas.
> - Lists all date ideas.

#### Dislikes

> - No filters, just a button for randomizing.
> - Can't save any ideas.
> - Poor ad placements.

---

3.  https://myspicyvanilla.com/

Claims to use "AI".

#### Likes

> - Has a function to sign up, will save your ideas.
> - Dates can be shared on Whatsapp and social media.

#### Dislikes

> - Design feels off, colour scheme seems like a poor choice, very dark.
> - Allows only 1 random date before being behind pay wall.

---

4.  https://lovewick.com/ (App)

#### Likes

> - Very professional design, what I aspire to be.
> - Have built on all aspects of dating.

#### Dislikes

> - Less emphasis on your own ideas being in rotation, more for people without ideas.
> - Non web based, all on the app.

---

With these observations I was ready to start designing my wireframes.

### **Wireframes:**

   <details><summary></summary>
   <img src="" alt="">
   </details>

---

## **Building Stage**

### **Colour Scheme And Theme:**

<img src="" alt="">

### **Typography**

After doing a little research into fonts, I found a useful [article](https://varrojoanna.com/the-easiest-fonts-for-kids-to-read/) talking about children and the fonts they find easiest to read, seeing as this game is aimed at a younger audience I thought it best to ensure that children were the focus when it came to the typography. I chose to use googles 'Andika' after reviewing all the recommendations, I felt this was the best middle ground for young and older players.

Titles use a font weight of 700 for a bigger bolder title, while the rules section uses the standard weight. The buttons use a weight of 600 to give it a little more weight than any paragraphs.

Given limited amount of text I felt Andika was good enough to cover all possible uses, if for some reason it isn't available font family will default to Helvetica and then sans-serif.

- All fonts were sourced from Google fonts, as stated in the credits.

---

## **Features**

Below are some of the features currently within the site.

### **Home Page:**

- The home page is big and bold, Using classic 'connect 4' colours for the text and buttons. After doing my research I really noticed the impact of not having a initial page to welcome the user, allowing them to read the rules before being thrown straight into a game.

<img src="assets/images/MSP2 home page.png" alt="image of the center of the home page">

### **Wallpaper And Back-panel:**

- As mentioned in the colour scheme section above my first job was to find a background that I was really happy with, it took a while and I originally struggled to find something that would be suitable for this site. I didn't want to spend too much time focusing on a background and "lose the momentum" of coding, so at the start I actually used the space background that made my wireframe.

- I liked the idea of a translucent back pack to help lift the content off the back wallpaper, I like this effect a lot as it helps give it a sense of depth. Given how much I liked the background I feel making it see through gave both the lifting effecting while also showing off the wallpaper.

<img src="assets/images/MSP2 full page.png" alt="image of the entire home page">

### **Hiding Pages:**

- After disusing numerous ideas with my mentor, he showed me a trick he likes to implement in his own code. Creating a HTML class and setting the CSS display to this class as "none".

<img src="assets/images/hide css.png" alt="image of .hide css">

- Using JS I am able to implement a simple event listener for a button click which will simply add the class to everything in the selected and then remove it from the page I wish to see. This is good as I am able to easily adapt and change this for future use, if I wanted to add another page I can add the "const" at the top with the correct value and extend the list.

<img src="assets/images/hide JS.png" alt="">

- With the site being a SPA (single page application) this allows for a few things to happen which benefit the site greatly.

  \*First the page and all JS loads in its entirety all before you click into the game, so if for any reason you had to wait for the JS in the background to load you wouldn't notice it as you are greeted by the home page.

  \*Secondly if you are playing the game and want to review the rules, you can click on rules, then click back and will return back to the same game state almost like a save. You never have to remember a games current state as its never removed, the user simply cannot see it.

### **Buttons:**

- My initial home page play and rules buttons are big and large, in the same colour red as the connect 4 tile, I am a big fan of CSS styling animations so I had a look online and found [a website](https://getcssscan.com/css-buttons-examples) with simple and professional looking hover animation, I was able to modify these to fit my purpose.

<img src="assets/images/MSP2 Home Buttons.png" alt="image of the home page buttons">

- The hover animation lifts the button up slightly, gives it a slight shadow and reduces the transparency. Again I feel this helps with the sense of depth on the page.

<img src="assets/images/MSP2 Home Button Hover.png" alt="image of the home page buttons with mouse hover">

- My navigation buttons are the same for consistency and contain a small icon.

<img src="assets/images/MSP2 Navigation Buttons.png" alt="image of the navigation buttons">

- When viewed on a small screen, these buttons shrink down to a more square shape and the inner text is hidden.

<img src="assets/images/MSP2 Navigation Buttons Hover.png" alt="image of the navigation  buttons with mouse hover">

### **Swap Sides:**

- Given the game is focused towards mobile users, I gave a lot of thought to the physical side of playing the game, if a user is left handed it would potential be uncomfortable if all the buttons are on the right hand side. The bottom button in the navigation buttons allows for buttons to swap sides. The image below shows the buttons on the left hand side of the screen.

<img src="assets/images/MSP2 Navigation Button Left .png" alt="Navigation buttons on left">

### **Rules:**

- With the game aimed at a younger audience there is a change someone has not played the game before, so I give a short explanation about the game.

- I implemented the red background to help contrast with the yellow font.

<img src="assets/images/MSP2 Rules.png" alt="Rules page">

### **Modal:**

- The modal is something I am very pleased with, due to the physical limitations of the game board on small screens this game has to be played landscape at certain screen widths. Using a [SWAL](https://sweetalert2.github.io/), a JS library I was able to get a professional looking modal.

<img src="assets/images/MSP2 Modal.png" alt="Initial pop up due to screen width">

- Using Javascript I am able to review the screen size, if the site is loaded up in a screen size I know wont support the site the user isn't allowed to access until the device is rotated. I am more than confident I was able to get the site working on the smallest possible mobile device width so it wont leave any users unable to play the game.

<img src="assets/images/MSP2 Modal Rotate.png" alt="rotation causing second pop up">

- Once the user has rotated the screen they get a big 'OK' button which will then allow them to play the game.

### **The Game:**

- The game in all honesty wasn't 100% what I wanted, my original idea was to have tiles be erased after scoring a '4 in a row' but I ran into numerous bugs and issues which were getting far too time consuming, if you wish to see any of these they will be visibly in my repository as I made a branch off my main to tackle this aspect of the game. Luckily planning to build Connect 4 first and then work in the column erasing element paid off.

- The game board is sat into the background, contrasting with the buttons and titles on the home page and rules page. I used a colour match with the background to help set this in and a border colour that is taken from the darkest part on the background to cement the board.

- A big bold "Current Player" title sits above the board, this way when the game is being playing between friends on a phone it can be passed back and forth and the player order is obvious.

- The game tiles marry up with the chosen colours on my palette.

<img src="assets/images/MSP2 Game Screen.png" alt="Game Screen">

### **Winner:**

- Once a player wins, the "Current player" display is hidden and the winner is shown, this text is much larger.

<img src="assets/images/MSP2 Win screen.png" alt="Winner screen">

### **Draw:**

- In the unlikely event of a draw (trust me its very difficult it took my multiple attempts to get this screen shot) the game will show act similarly to a win, with "Draw!" replacing the current player.

<img src="assets/images/MSP2 Draw Screen.png" alt="Draw screen">

### **Restart:**

- Due to how the game was made and all the modifications I made thereafter, the restart button does a few things in sequence, it:
  1.  Resets the gameOver variable back to false
  2.  Resets the game, which in turn had to be modified to see if a game board already existed, if it does it removes and recreates.
  3.  Resets the winner.
  4.  Resets the first turn back to red.

Although its a simply function I was rather proud of it, as it was modified numerous times as the site evolved.

### **Tab Icon:**

- I found a cool tab [favicon!](https://www.iconarchive.com/show/free-flat-sample-icons-by-thesquid.ink/space-rocket-icon.html#google_vignette) strangely enough this feels like the most "developery" thing I have done so far.

<img src="assets/images/MSP2 Tab Icon.png" alt="Browser Tab Icon">

### **404:**

- A simple 404 if something goes wrong, which links

<img src="assets/images/MSP2 404 Page.png" alt="404 page">

---

## **Testing**

I tested the site throughout the development phase using the following:

- Apple Macbook air 13"
- Iphone 15 Pro Max

I also used Google dev-tools during development, ensuring responsiveness across all screen sizes.

- All links on homepage.html and 404.html have been tested and are in working order.

### **Validator Testing:**

#### **CSS:**

After running the site through the CSS validator I got no errors.

<img src="assets/images/MSP2 CSS validation.png" alt="CSS validator proof">

#### **HTML:**

After running the site through the HTML validator I got 5 errors.

<img src="assets/images/MSP2 HTML validation.png" alt="HTML validator initial run proof">

- 2 errors for the 2 home page buttons, the text was sat within a H2 tag. This has now been changed to the text sitting within the button and a new class being made that overrides the generic buttons styling.

- 2 errors for unclosed div's, throughout the build process I had been moving parts around to change how they appear, in this process I had accidentally removed some div's closing tags. This has been resolved and the site was unaffected.

- The final error for the body resolved itself once the above was fixed and retested.

<img src="assets/images/MSP2 HTML validation complete.png" alt="HTML validator 0 error proof">

#### **Javascript:**

I ran my JS code through 2 validators.

JSHint:

- Running my JS through JSHint I got 2 undefined variables, this was not a concern as "SWAL" is an external library that the validator could not see.

<img src="assets/images/JSHint.png" alt="JSHint validator">

ValidateJavaScript:

- ValidateJs showed a lot more issues, mainly that I had no JSDoc comment on any of my functions, I had been using a commenting habit I had developed during the last project, after seeing this I went through all my functions and documented them all properly.

- Line length was also an issue for a couple comments, using the validator I identified the lines effected and reduce comment length.

<img src="assets/images/ValidateJS.png" alt="ValidateJS validator">

- I have one remaining error which at this moment I can't resolve, it doesn't break the code so at this moment in time I have had to leave, this will be reviewed later to ensure this isn't a repeat offender in later works.

<img src="assets/images/this error.png" alt="this error">

### **LightHouse Testing:**

Using the LightHouse in my Google DevTools I was able to optimize my website for Performance, Accessibility, SEO and best practices.

<img src="assets/images/Lighthouse mobile.png" alt="Lighthouse mobile scores">

- I was happy with my score on mobile, next came desktop which showed I wasn't optimized on "SEO"

<img src="assets/images/Desktop SEO failure.png" alt="Lighthouse Desktop SEO score">

After reviewing the lighthouse results I was able to implement a meta tag in my head section with a description summarizing the content of the page.

<img src="assets/images/Lighthouse Desktop.png" alt="Lighthouse Desktop improvement">

Along with all validator testing the site has been tested on numerous computers and phones as I have had friends and family review the site.

## **Future-Enhancements**

The following is a list of future enhancements that I would like to implement given more time and/or knowledge.

- The Tetris element, starting out my main goal was to get this site fully functioning and bug free which I am happy I achieved, but to really make this project stand out and to warrant it being online I wanted to bring a new idea to a classic. Due to numerous issues that I simply do not have the skills to resolve in the time frame I have, I had to scrap.

- A change in theme, as shown in my initial wireframes I was interested in the idea of changing the overall theme depending on the users preference. This would include the background image them being selected from a number of natural scenes and the colour of the tiles being selected from a colour wheel from the rules/settings menu.

- I spent a long time trying to implement the tiles being meteors, I was really trying to avoid having a connect 4 board just sat on top of a background.

- Given more time and skill I would have liked to modify the board its self so it sat behind a themed image, so it looked like the board was part of the theme. With the current space theme if could have been made of rockets or made to look like a space station.

- If I was looking to release this website to be played between friends I would like to introduce a way of playing with a friend on a different machine, so the 2 players wouldn't need to share a screen, this was something I noticed during my research.

- Animation, I would like to implement 2 forms of animation, one being a drop animation that would simulate a tile piece falling, the other being the tile floating about the board following a curser or finger. I feel this would help add a sense of realism and it is one of the few physical elements to the game, which could feel lost on the digital format.

- Having reviewed everything during the final steps of this project I feel like the winner/draw screens could do with a bigger replay button in the center of the screen, at the moment the players would need to reselect from the navigation buttons.

## **Deployment**

The site was deployed to GitHub pages. The steps to deploy are as follows:

- From this project's repository, navigate to the settings tab

- From the left hand menu, select pages.

- From the source section drop-down menu, select the Main Branch.

- Once the main branch has been selected, the page will refresh and provide a link to the live project.

You can find the live site via the following URL - https://lukethornton92.github.io/Milestone-Project-2-C4/

---

## **Credits**

### **Honorable Mentions:**

This project could not have happened without the support of the following people listed in no particular order:

- Jessica Goff, for putting up with me spending many evenings getting frustrated with JS.

- Richard Wells, a brilliant mentor keeping my on track.

- Work colleagues, they actually came up with the name have been very keen to play the game.

### **General Reference:**

- I relied upon W3schools, ChatGPT and stack overflow for general references throughout the project.

### **Content:**

- All content was written by myself

- Accessibility checker - [WAVE - Web accessibility evaluation tool](https://wave.webaim.org/)

- Button Icons - https://fontawesome.com/

- Fonts - https://fonts.google.com/specimen/Andika

- Button CSS - https://getcssscan.com/css-buttons-examples

### **Media:**

- Wallpaper - https://www.vecteezy.com/vector-art/1110375-stars-and-planets-in-outer-space

- Favicon - https://www.iconarchive.com/show/free-flat-sample-icons-by-thesquid.ink/space-rocket-icon.html#google_vignette
