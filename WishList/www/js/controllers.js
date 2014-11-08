angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope, $ionicModal, $timeout) {
	// Form data for the login modal
  $scope.loginData = {};

  // Create the login modal that we will use later
  $ionicModal.fromTemplateUrl('templates/login.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modal = modal;
  });

  // Triggered in the login modal to close it
  $scope.closeLogin = function() {
    $scope.modal.hide();
  };

  // Open the login modal
  $scope.login = function() {
    $scope.modal.show();
  };

  // Perform the login action when the user submits the login form
  $scope.doLogin = function() {
    console.log('Doing login', $scope.loginData);

    // Simulate a login delay. Remove this and replace with your login
    // code if using a login system
    $timeout(function() {
      $scope.closeLogin();
    }, 1000);
  };
})

.controller('FriendsCtrl', function($scope, Friends) {
  $scope.friends = Friends.all();
})

.controller('FriendDetailCtrl', function($scope, $stateParams, Friends) {
  $scope.friend = Friends.get($stateParams.friendId);
})

.controller('AccountCtrl', function($scope) {
})

.controller('ApplyEMI', function($scope) {
})

.controller('Login', function($scope) {
	$scope.config = {
			server : 'localhost'
		}

	$scope.results = [];
	var dummy = [{name : "pallal"},{name : "pallal"},{name : "pallal"},{name : "pallal"},{name : "pallal"}]
	$scope.sPopulateText = function(data)
	{	
		var s = "";
		for(var i in data)
		{
			s = '<div class="card">\
					<a class="item item-thumbnail-left" href="#">\
					  <img src="img/quadcopter.jpg">\
					  <h2>'+data[i].name+'</h2>\
					  <p>Nine Inch Nails</p>\
					  <span class="emi">EMI: 12%</span>\
					</a>\
				</div>';
			$scope.results.append(s);
		}
		
	}
	
	sPopulateText();
	
	
	
	
});