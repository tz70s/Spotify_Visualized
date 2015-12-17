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

		$.getJSON($SCRIPT_ROOT + '/biodef',function(data) {
			$("#biography").text(data["artist"]["biographies"][0]["text"]);
		});

    	$.getJSON($SCRIPT_ROOT + '/defsongs', 
    		function(data) {

    			var top_tracks = [];
    			var tracks_name = [];
    			for (var i = 0; i < data["tracks"].length ; i++) {
    				top_tracks.push(data["tracks"][i]["preview_url"]);
    				tracks_name.push(data["tracks"][i]["name"]);
    			}

	    		var oricount = 0;
		    	var audio = document.getElementById("player");

		    	var orisong = [];
		    	orisong.push(document.getElementById("song1"));
		    	orisong.push(document.getElementById("song2"));
		    	orisong.push(document.getElementById("song3"));
		    	orisong.push(document.getElementById("song4"));
		    	orisong.push(document.getElementById("song5"));
		    	orisong.push(document.getElementById("song6"));
		    	orisong.push(document.getElementById("song7"));
		    	for (var i = 0; i < 7; i++ ){
		    		if(tracks_name != ""){
		    			$(orisong[i]).text(tracks_name[i]);
		    		} else {
		    			$(orisong[i]).text("");
		    		}
		    	}
		    	audio.src = top_tracks[oricount];
		    	audio.volume = 0.4;
		    	orisong[oricount].style.backgroundColor = "#B0E0E6";
		    	audio.load();
				audio.play();
		    	audio.addEventListener("ended", function() {
		    				orisong[oricount].style.backgroundColor = "#FFFFFF";
		    				oricount++;
						    audio.src = top_tracks[oricount];
						    orisong[oricount].style.backgroundColor = "#B0E0E6";
						    audio.load();
						    audio.play();
				});
    	});

    	
});


