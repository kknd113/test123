$(document).ready(function() {
	var page = 0;
	var scroll_activated = false;

	var data = {
		page: page,
	};
	$.ajax({
		type: "POST",
		url: "/dashboard",
		data: JSON.stringify(data),
		contentType: "application/json",
		dataType: "json",
	}).done(function(data) {
		goals = jQuery.parseJSON(data['goals']);
		goals.forEach(function(entry) {
			console.log(entry);
			fields = entry['fields'];
			user = $(".users>#id"+fields['creator']);
			console.log(fields);
			$(".dashcard-container").append('<li><div class="dashcard" id="'+entry['pk']+'"></div></li>');
			$(".dashcard#"+entry['pk']).append('<div class=dashcard-title><a href="/goals/'+entry['pk']+'">'+fields['title']+'</a></div>');
			$(".dashcard#"+entry['pk']).append('<div class=dashcard-creator><b>Creator:</b> <a href="/users/'+fields['creator']+'">'+user.text()+'</a></div>');
			$(".dashcard#"+entry['pk']).append('<div class=dashcard-prize><b>Prize:</b> '+fields['prize']+'</div>');
			$(".dashcard#"+entry['pk']).append('<div class=dashcard-description>'+fields['description']+'</div>');
			// $("tbody").append('<tr><td><a href="/goals/'+entry['pk']+'">'+fields['title']+'</a></td>'+
			// 	'<td>'+fields['description']+'</td>'+
			// 	'<td><a href="/users/'+fields['creator']+'">'+user.text()+'</a></td>'+
			// 	'<td>'+fields['prize']+'</td></tr>')
		});

	}).fail(function(data) {
		console.log(data);
		alert("failure");
	});
	page = 1;

	$(window).scroll(function() {
	   if($(window).scrollTop() + $(window).height() == $(document).height() && !scroll_activated) {
	        scroll_activated = true;
			var data = {
				page: page,
			};
			$.ajax({
				type: "POST",
				url: "/dashboard",
				data: JSON.stringify(data),
				contentType: "application/json",
				dataType: "json",
			}).done(function(data) {
				goals = jQuery.parseJSON(data['goals']);
				goals.forEach(function(entry) {
					console.log(entry);
					fields = entry['fields'];
					user = $(".users>#id"+fields['creator']);
					console.log(user);
					$(".dashcard-container").append('<li><div class="dashcard" id="'+entry['pk']+'"></div></li>');
					$(".dashcard#"+entry['pk']).append('<div class=dashcard-title><a href="/goals/'+entry['pk']+'">'+fields['title']+'</a></div>');
					$(".dashcard#"+entry['pk']).append('<div class=dashcard-creator><b>Creator:</b> <a href="/users/'+fields['creator']+'">'+user.text()+'</a></div>');
					$(".dashcard#"+entry['pk']).append('<div class=dashcard-prize><b>Prize:</b> '+fields['prize']+'</div>');
					$(".dashcard#"+entry['pk']).append('<div class=dashcard-description>'+fields['description']+'</div>');
					// $("tbody").append('<tr><td><a href="/goals/'+entry['pk']+'">'+fields['title']+'</a></td>'+
					// 	'<td>'+fields['description']+'</td>'+
					// 	'<td><a href="/users/'+fields['creator']+'">'+user.text()+'</a></td>'+
					// 	'<td>'+fields['prize']+'</td></tr>');
				});

			}).fail(function(data) {
				console.log(data);
				alert("failure");
			});
			scroll_activated = false;
			page = page + 1;	
	   }
	});
});
