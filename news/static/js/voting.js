function vote(elemId, target) {
	var elem = document.getElementById(elemId);
	var votingLabel = elem.getElementsByClassName('votes')[0];
	var value;
    if (target == 'down'){
    	value = -1;
    } else if (target == 'up') {
    	value = 1;
    }
    $.ajax({
		url: "setvote/?id=" + elemId + "&value=" + value,
		dataType: "text",
		success: function(data){
			votingLabel.innerHTML = data;
		},
		error: function(error){
			console.log("An unexpected error occurred: " + error);
		}
	});
    
}


(
   function($){
        $.fn.shuffle = function() {
           return this.each(function(){
               var items = $(this).children();
                return (items.length)
                   ? $(this).html($.shuffle(items,$(this)))
               : this;
           });
       }
        $.fn.validate = function() {
           var res = false;
           this.each(function(){
               var arr = $(this).children();
               res =    ((arr[0].innerHTML=="1")&&
                   (arr[1].innerHTML=="2")&&
                   (arr[2].innerHTML=="3")&&
                   (arr[3].innerHTML=="4")&&
                   (arr[4].innerHTML=="5")&&
                   (arr[5].innerHTML=="6"));
           });
           return res;
       }
        $.shuffle = function(arr,obj) {
           for(
           var j, x, i = arr.length; i;
           j = parseInt(Math.random() * i),
           x = arr[--i], arr[i] = arr[j], arr[j] = x
       );
           if(arr[0].innerHTML=="1") obj.html($.shuffle(arr,obj))
           else return arr;
       }
    })(jQuery);
    $(function() {
		$("#sortable").sortable();
		$("#sortable").disableSelection();
		$('ul').shuffle();
		$("#captchasubmit").click(function () {
			if ($('ul').validate()) {
				document.getElementById('captcha').setAttribute('style','display: none');
				var voteInfo = document.getElementById('captcha').getAttribute('vote').split(':');
				vote(voteInfo[0], voteInfo[1]);
				document.getElementById('captcha').removeAttribute('vote');
				alert("Ваш голос учтен!");
			} else {
				alert("Попробуйте еще раз!");
			}
			$('ul').shuffle();
		});
});