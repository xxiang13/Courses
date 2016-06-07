var module = angular.module('listApp', []); //create an Angular module

//create an Angular controller named listController and use the initController function to initialize the controller
var controller = module.controller('listController', initController);


function initController($scope) {    
    $scope.items = ['First Item'];
    $scope.addItem = function() {

    //test if the newItem property of the controller's scope has a value that is not null or undefined
        if ($scope.newItem) { 
    //push the new item into the array stored as the items property of the controller's scope
            $scope.items.push($scope.newItem); //append value to list items
            $scope.newItem = undefined; //refresh newItem
        }        
    }
}
