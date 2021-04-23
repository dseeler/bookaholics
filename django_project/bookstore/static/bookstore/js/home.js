function setStars(id, rating, type){
    let stars = "";
    for (let i = 0; i < 5; i++){
        if (i < rating){
            stars += "<span class='fa fa-star checked'></span>";
        }
        else{
            stars += "<span class='fa fa-star'></span>";
        }
    }

    document.getElementById(type + "-rating-" + id).innerHTML = stars;    
}