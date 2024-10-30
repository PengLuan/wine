$(function(){
	let BaseUrl = "http://127.0.0.1:5000/chat";
	let ScoreUrl = "http://127.0.0.1:5000/score";
	const UUID = crypto.randomUUID();
	$("#send").click(function(){
		let text = $("#text").val();
		if(text){
			$("#container").append("<div class='for-human'>" + text + "</div>")
			$.post(BaseUrl, {"text": text, "session_id": UUID}, function(res){
				if(res.code == 0){
					$("#container").append("<div class='for-robot'>" + res.data.flat_content + "</div>");
					if (res.data.wine_id > 0){
                        $("#can_do_score").show();
                        $("#wine_name").text(res.data.wine_name);
					}
				}
				console.log(res);
			});
		}else{
			alert("请输入聊天内容")
		}
	});
	$("#no_score").click(function(){
        $("#can_do_score").hidden();
	});
	$("#yes_score").click(function(){
        $("#can_do_score").hidden();
        $("#score").show();
	})
	$("#do_score").click(function(){
		let desc = $("#desc").val();
		let star = $("#score_value").val();
		if(text){
			$.post(ScoreUrl, {"desc": desc, "star": star, "session_id": UUID}, function(res){
				if(res.code == 0){
					$("#container").append("<div class='for-robot'>" + res.data.flat_content + "</div>");
				}
                $("#score").hidden();
				console.log(res);
			});
		}else{
			alert("请输入聊天内容")
		}
	});
});