# R Standards
Initial Creator: [Joe Ratterman](https://github.com/JoeRatterman-AMEND)

# Table of Contents
1. [Introduction](#introduction)
2. [Code Layout](#code-layout)
3. [Naming Conventions](#naming-conventions)
4. [Loading & Installing Packages](#imports)
5. [Comments](#comments)
6. [Security](#security)

# Introduction
This document serves to provide coding conventions for R.

This document draws consolidates information from various other published style guides. Primarily the Tidyverse Style Guide (https://style.tidyverse.org/) & Hadley Wickham's Style Guide (http://adv-r.had.co.nz/Style.html). This is intended to be a living document that can be updated as additional functionality / features become available in R.

This is to serve as a **guideline**. Do not waste excess time to conform to standards but do your best to use them as described in this document from the begining of a project.

# Code Layout

- Maximum line length is **80 symbols**
- Use blank lines sparingly
- Use '-' or '=' to break between sections of code
- All operators should have spaces on both sides (=, +, -, <-, etc.)

```r
# good
total_inches <- (total_feet / 12)

# bad
total_inches <-(total_feet/12)
```
- Spacing should not be used before or after an opening parenthesis

```r
# good
my_function(var_1, var_2)

# bad
my_function (var_1, var_2)
my_function( var_1, var_2)
```
- Add a space around the criteria call in ```for```, ```while```, ```if```:
```r
# good
for (i in 1:length(obj)) {
  action(x)
} 

# bad
for(i in 1:length(obj)){
  action(x)
} 
```

- When using an opening bracket ```{```, it should be the last character in the line:
```r
# good
for (i in 1:length(obj)) {
  action(x)
} 

# bad
for(i in 1:length(obj)){action(x)} 
```

- When using a closing bracket ```}```, it should be the first character in the line. It should also align with the function that opened the brace: 
```r
# good
for (i in 1:length(obj)) {
  
  if (i < 5) {
  
    # do this
    
    } else {
     
     # do that
    
    }

} 

# bad
for (i in 1:length(obj)) {
  
  if (i < 5) {
  
    # do this
    
} else {
     
     
    
 # do that   }

  } 
```


- Add extra rows when it makes code more readable
```r
# good
my_list = c('this is a really long string',
            'this is another really long string', 
            'this is a third really really long string'
            )

# bad
my_list = c('this is a really long string', 'this is another really long string', 'this is a third really really long string')
```

- When calling a function with several arguments, use multiple lines as needed for readability
```r
# good
my_function(
  a = "this is a long & complex value", 
  b = "this is a second long & complex value", 
  c = "this is a final long & complex value"
)

# bad
my_function(a = "this is a long & complex value", b = "this is a second long & complex value", 
  c = "this is a final long & complex value"
)
```
Note that the comma separating arguments should appear at the end of each line **Not** the beginning of the new line.

# Naming Conventions

Dataframes, variables, and function names should always be lowercase using ```_``` as needed. Names should be as short as possible, while still being understandable. A few examples are below. 

**Do Nots:**
- CamelCase
- Multiple words without a ```_``` to separate should not be used
- Start name with a number
- Capital letters

```r
# good
boxscore_df # Dataframe
total_points # Variable
avg_points # Variable
calc_total_points # Function

# bad
BoxscoreDF # Dataframe
2020Boxscore_df # Dataframe
MYVARIABLENAME # Variable
Total_Points # Variable
AvgPoints # Variable
really_complex_function_with_long_name # Function
```

# Loading & Installing Packages
There are two primary functions that are used to load packages in R: ```library()``` and ```require()```. The only practical difference is that ```library``` will return an error if a package is not installed, while ```require``` only returns a warning message. While both will work, ```library()``` is preferred as it will stop a script before trying to run a function from the loaded package. 

Installing packages should always be completed in the Console or Command Prompt with ```install.packages()```. **Never** install a package in a script, as it can lead to issues with package versions. 

# Comments
Comments should be concise and used as needed. Use comments to explain the 'why' of the code, not the 'what'.

**General Guidelines**
- If the code needs comments to clarify its work, you should consider refactoring or rewriting it. "The best comments to code are the code itself"
- Make sure comments are updated as code is changed
- Use complete sentences
- Comments still follow the same style rules as the rest of the code. If a comment exceeds the maximum number of characters, use a comment block instead
- Begin comments with a single ```#``` followed by a space: 
```r
# good comment

#this is a bad comment

# this is a bad comment even though I have added the space this is still a run-on sentence and it is going to be over the recommended 80 character limit so it would need a lot of work to fix it.
```

# Security
To avoid security breaches, we will be using the package keyring. Keyring is used to save passwords in a computer's credential store. After setting a password once, it can be retrieved. This way, passwords do not need to be saved in a script - reducing the risk of them being seen by outsiders. 

To set a password: 
```r
# Load keyring
library(keyring)

# Set password
key_set_with_value(
  service = "domain", 
  username = "your_address@example.com",
  password = "password_string"
)

# Retrieve password
key_get("user_email", "your_address@example.com")

```

- ```domain``` is the client name (for code belonging to the logan-rollchocks repo, ```domain = 'logan'```. for bw-elt-meltanodbt, ```domain = 'bw'```)
- keyring works by storing the ```password_string``` with a combination of ```domain``` and ```username``` on your os. This means two important things:
- The ```key_get()``` function will only work on your computer or a computer where the ```key_set_with_value()``` function has already been done
- Once the ```key_set_with_value()``` function has been called, ```key_get()``` can be called on ANY python script run on your computer
- **NEVER** push code with a plain string password to GitHub
