
	
function formatType(value){
	return "<img src='" + MYMEDIA + value + "' alt='Photo' width='64' height='64'/>";
}

function findNews() {
    console.log('here');
    var url = "&filter=" + JSON.stringify({'name__contains': document.getElementById('findByName').value});
    setStore(url);
}
function makeForm(news_list) {
    if ($('#info')[0])
        $('#info')[0].remove();
    var infoPanel = $("<div/>",{
        class: "row",
        id: "info"
    });
    infoPanel.appendTo('div#cpane');
    for (var i = 0; i < news_list.length; i++) {
        var mystory = $("<div/>",{
          class : "col shadow-cp",
          style: "width: 300px; flow:left; height: 420px; margin:5px;"
        });
        var tmbn = $("<div/>",{
          class : "thumbnail"
        });
        var span = $("<span/>",{
          class: "imgPicture"
        });
        span.appendTo(tmbn);
        var img = $("<img/>",{
          src: MYMEDIA + news_list[i]['photo'],
          height: "auto",
          width: "290"
        });
        img.appendTo(span);
        var caption = $("<div/>",{
          class : "caption"
        });
        caption.appendTo(tmbn);
        var header = $("<H3/>",{
          text: news_list[i]['name']
        });
        var text = $("<p/>",{
          text: news_list[i]['text'].substr(0, 300)
        });
        var href = $("<a/>", {
            href: '/vote/' + news_list[i]['id'],
            text: '...Читать далее...'
        })
        href.appendTo(text);
        header.appendTo(caption);
        text.appendTo(caption);
        tmbn.appendTo(mystory);
        mystory.appendTo("div#info");
    }
}

function setStore(extUrl) {

	$.get({
        url: window.location.origin + "/?" + extUrl,
		dataType: "json",
		success: function(data){
            console.log(data);
            var news_list = data['news'];
            
            makeForm(news_list);

		},
		error: function(error){
			console.log("An unexpected error occurred: " + error);
		}
    })
}