var app = angular.module('navigationApp', ['ngRoute']);
app.controller('listController', function ($scope, model) {
    $scope.items = model.getAll();
});
app.controller('detailController', function ($scope, $routeParams, model) {
    $scope.itemId = $routeParams.itemId
    $scope.item = model.get($scope.itemId);
});
app.config(function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl : 'home.html'
        })
        .when('/list', {
            templateUrl : 'list.html',
            controller  : 'listController'
        })
        .when('/detail/:itemId', {
            templateUrl : 'detail.html',
            controller  : 'detailController'
        })
        .otherwise({redirectTo : "/"});
});
app.factory ('model', function () {
    var data = [
        { id: 0, title: 'Degree', icon: 'img/degree.png', description: 'First, you might graduate from college.' },
        { id: 1, title: 'Networking', icon: 'img/networking.png', description: 'Then you could network with colleagues.' },
        { id: 2, title: 'Certification', icon: 'img/certification.png', description: 'Earn a certification to stay ahead of the pack' },
        { id: 3, title: 'Job Hunt', icon: 'img/jobhunt.png', description: 'Take your network and certifications on the hunt for the coolest jobs.' }
    ];
    return {
        getAll:function () {
            return data;
        },
        get:function(id){
            return data[id];
        }
    };
});