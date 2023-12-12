function toogleSideBar() {
	console.log("side-bar-open-btn clicked");
	let sideBar = $("#side-bar");
	let self = $("#side-bar-open-btn")[0];
	let body = $("#body")[0];
	if (sideBar.hasClass("show-bar")) {
		sideBar[0].style.width = "0";
		sideBar.removeClass("show-bar");
		self.style.marginLeft = "0";
		body.style.marginLeft = "0";
	} else {
		sideBar[0].style.width = "250px";
		sideBar.addClass("show-bar");
		self.style.marginLeft = "250px";
		body.style.marginLeft = "250px";
	}
}

// $("#side-bar-open-btn").on("click", function () {
// 	console.log("side-bar-open-btn clicked");
// 	let sideBar = $("#side-bar");
// 	if (sideBar.hasClass("side-bar-show")) {
// 		sideBar.removeClass("side-bar-show");
// 	} else {
// 		sideBar.addClass("side-bar-show");
// 	}
// });