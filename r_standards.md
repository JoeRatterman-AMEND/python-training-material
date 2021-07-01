# R Standards
Initial Creator: [Joe Ratterman](https://github.com/JoeRatterman-AMEND)

# Table of Contents
1. [Introduction](#introduction)
2. [Code Layout](#code-layout)
3. [Naming Conventions](#naming-conventions)
4. [Imports](#imports)
5. [Comments](#comments)
6. [Security](#security)
7. [Linters](#linters)
8. [Doughnuts](#doughnuts)

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

- When using an opening bracket ```{```, it should be the last character the line
```r
# good
for (i in 1:length(obj)) {
  action(x)
} 

# bad
for(i in 1:length(obj)){action(x)} 
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
