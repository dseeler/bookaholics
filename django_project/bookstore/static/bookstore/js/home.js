function setStars(id, rating){
    let stars = "";
    for (let i = 0; i < 5; i++){
        if (i < rating){
            stars += "<span class='fa fa-star checked'></span>";
        }
        else{
            stars += "<span class='fa fa-star'></span>";
        }
    }

    document.getElementById("rating-" + id).innerHTML = stars;    
}