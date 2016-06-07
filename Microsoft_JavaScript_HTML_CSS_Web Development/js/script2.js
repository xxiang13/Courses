
// JavaScript logic to retrieve an object to manipulate the section element with an id of output
var elem = document.getElementById('output');  

// Add another line of JavaScript logic to update the element's innerHTML property to the following value 
elem.innerHTML += 'Test'

// Observe that the text on the page now reads "10". > I
// In JavaScript, simple addition was performed between two numbers. The numeric result is then converted to a string
elem.innerHTML += 4 + 6;

// Observe that the text on the page now reads "10 Demo". > Expressions are evaluated from left to right. 
// First the numbers were added together (10). 
// Than you have a number and a string. At this point, you have to perform string concatenation to end up with "10 Demo".
elem.innerHTML += 4 + 6 + ' Demo';

// Observe that the text on the page now reads "Demo 46". > Expressions are evaluated from left to right. 
// First the string and number were concatenated to form "Demo 4" Than the number 6 was concatenated to form "Demo 46"
elem.innerHTML += 'Demo ' + 4 + 6;

// Observe that the parentheses overrode the left-to-right evaluation order. The text is now "Demo 10
elem.innerHTML += 'Demo ' + (4 + 6);