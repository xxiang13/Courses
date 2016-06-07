var module = angular.module('demoApp', []);

//create the Angular controller and use the initController function to initialize the controller
var controller = module.controller('demoController', initController);

//use scope * and*http as the parameters for this function
function initController($scope, $http) {    
    $http.get('http://httpbin.org/ip') //chain an anonymous method to handle the response for this HTTP request
        .then(function(response) {
        //Within the anonymous method, use the following lines of code to parse and utilize the HTTP response
            $scope.resultJSON = JSON.stringify(response);
            $scope.resultProperty = response.data.origin;
        });    
}



