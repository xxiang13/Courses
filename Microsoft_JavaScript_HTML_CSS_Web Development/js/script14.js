function makeRequests() {
    
    //Observe the JSON response shown in your alert dialog.
    $.getJSON('http://httpbin.org/ip')
        .done(function(response) {
            alert(JSON.stringify(response));
            $('body > p').text(
                response.origin
            );
        });
}

$(document).ready(function () {
    makeRequests();
});

