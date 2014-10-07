app.controller('main', function($scope, $http, $timeout) {
	var poll = function() {
		$timeout(function() {
			$http.get('/generate').
				success(function(data) {
					$scope.data = data;
				}),
			poll();
		}, 500);
	};     
	poll();
});