/* Now i'm going to define angular module. So, angular.module,
   and I'm going to call this basic app.

   Now when I define angular.module, I define any dependencies that are necessary, I don't have any right now. 
   So I'm just going to store this module in a variable called 'app'. Now, I can say app.controller
   and I can define my first controller.
   So I am going to say, this is the homeController
   and if I need access to anything I can access it here.
*/

var app = angular.module('basicApp', []);

// So for the purposes of this homeController, I do you want to access the scope,
// that's where my module is located. So for my app.controller point of view I have access to the scope.
app.controller('homeController', function ($scope) {
   $scope.uname = "demouser";
    $scope.testMe = function () {
        $scope.uname += "123";
    };
});