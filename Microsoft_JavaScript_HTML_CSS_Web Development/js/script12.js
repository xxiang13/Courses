//add the following block of JavaScript 
//that will run the anonymous callback method after the DOM is loaded
$(document).ready(function () { //Within the anonymous callback method, add an invocation of the manipulateDOM function
    manipulateDOM();
});

function manipulateDOM() {
	var h1Headers = $('h1'); //get all h1 headers in the DOM
	h1Headers.text('Hello World'); //set the text of the elements to Hello World

	var h3Headers = $('h3'); //get all h3 headers in the DOM
	h3Headers.css('color', '#37887D'); //set the foreground color of the elements to a shade of green
	h3Headers.first().css('text-decoration', 'line-through'); //add a strike-through line to the first element in the list


	var lastH3Header = $('h3:last'); //get the last h3 header in the DOM
	lastH3Header.css('background-color', '#53226A'); //set the background color of the element to a shade of purple

}

