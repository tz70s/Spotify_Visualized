$.ajax({
		url: $SCRIPT_ROOT + '/default',
		type: "GET",
		dataType: "json",
		success: function(Jdata)
		 {
			//$("#post").text(Jdata["artists"]["items"][0]["name"])
			$("#artist-name").text(Jdata["artists"]["items"][0]["name"]);
			var uri = Jdata['artists']['items'][0]['uri'];

			var pics_src = Jdata['artists']['items'][0]['images'][0]['url'];
			$("#profile-pic").attr('src' , pics_src);

			var genre_length = Jdata['artists']['items'][0]['genres'].length;
			if( genre_length !== 0) {
				$("#genre-display").text(Jdata['artists']['items'][0]['genres'][0]);
				alert("not zero");
			} else {
				$("#genre-display").text("No Genre Display");
			}

			var followers_src = "https://embed.spotify.com/follow/1/?uri=" + uri + "&size=basic&theme=light";
			$("#followers").attr('src', followers_src);

		 },
		 error: function() {
		 	alert("ERROR!!!");
		 }

});

$(function() {
    	$.getJSON($SCRIPT_ROOT + '/defsongs', 
    		function(data) {
    			var play_string = "https://embed.spotify.com/?uri=spotify:trackset:";
    			for (var i = 0; i < data["tracks"].length ; i++) {
    				play_string += data["tracks"][i]["id"];
    				play_string += ","
    			}
    			$('#playlist').attr('src',play_string);
    		})
});