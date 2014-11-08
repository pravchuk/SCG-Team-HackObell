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
  
  //UIFUNCTION - Pallal
	$scope.wishlist = [];
	
  
  //
  
  

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

  $scope.doBarcode = function(){
	  	cordova.plugins.barcodeScanner.scan(
	      function (result) {
	          alert("We got a barcode\n" +
	                "Result: " + result.text + "\n" +
	                "Format: " + result.format + "\n" +
	                "Cancelled: " + result.cancelled);
	      }, 
	      function (error) {
	          alert("Scanning failed: " + error);
	      }
	   );
//alert("hi");
  }

})

.controller('FriendsCtrl', function($scope, Friends) {
  $scope.friends = Friends.all();
})

.controller('FriendDetailCtrl', function($scope, $stateParams, Friends) {
  $scope.friend = Friends.get($stateParams.friendId);
})


.controller('AccountCtrl', function($scope) {
})

.controller('LoginCtrl', function($scope,$http) {
	//alert("hi");
	var recDiv = document.getElementById('recomended');
	var dummy = [{name : "pallal",company : "PNP", emi : "14.5%"},{name : "pallal",company : "PNP", emi : "14.5%"}];
	//$scope.results = dummy;
	$scope.recomended = dummy;
	$scope.results = [];
	
	
	/*
	$scope.xhr1 = new XMLHttpRequest();
	$scope.xhr1.onreadystatechange = function ()
	{
		if($scope.xhr1.readyState == 4 && $scope.xhr1.status==200)
		{
		//alert("xhr success"+$scope.xhr1.readyState);
			$scope.disable();
			$scope.results = JSON.parse($scope.xhr1.responseText);
		}//functionality for updating the results;
	}
	*/
	
	$scope.add = function(i){
		$scope.wishlist.push($scope.results[i]);
		console.log(i,$scope.results[i]);
	}
	
	var handler = function(data)
	{
		//alert('hi');
		$scope.disable();
		//console.log(data);
		//for(var i in data)
		//{
			$scope.results = data;
			//console.log("Check : ",$scope.results);
		//}
		//functionality for updating the results;
	}

	$scope.disable = function(){
		var recDiv = document.getElementById('recomended');
		recDiv.style.display = "none";
	}
	
	$scope.keyPressed1 = function(ev)
	{
		//alert("hi");
		 ev = ev || event;
		 if(event.target.value=='') {var recDiv = document.getElementById('recomended');
			recDiv.style.display="block";
			$scope.results =[];
		 } 
		//$scope.xhr1.abort();
		//$scope.xhr1.open("GET","http://localhost/test.php?query="+ev.target.value,true);
		//alert("http://192.168.43.57/test.php?query="+ev.target.value);
		//$scope.xhr1.send();
		else 
		$http.get("http://localhost:8080/test.php?query="+ev.target.value).success(handler);
		
	}
	
	
})

.controller('ApplyEMI', function($scope) {
  
});
