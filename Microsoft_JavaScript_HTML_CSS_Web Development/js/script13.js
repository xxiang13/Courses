function makeRequests() {

$.ajax({ //invoke the $.ajax jQuery method
	//Use the following settings to configure the invocation of the $.ajax jQuery method
	url: 'http://www.example.com/api', //script 1
	//In this example, we are purposefully calling an API that does not exist to test the error functionality.
	method: 'GET',
	dataType: 'json'
})
	
    .done(function(response) { //adding a chained method invocation to handle if this request succeeds
        $('body > p').text(
            JSON.stringify(response)
        );
    })

    .fail(function() { //add the chained method invocation to handle if this request fails
        alert('An error has occured')
    });

}

$(document).ready(function () {
    makeRequests();
});

