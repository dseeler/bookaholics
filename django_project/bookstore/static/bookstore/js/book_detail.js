window.onload = (event) => {
    // Add rating stars
    const rating = $("#book-rating").html();
    for (let i = 0; i < rating; i++){
        $("#star" + i).addClass("checked");
    }

    // Add random number of ratings
    const num = Math.floor((Math.random() * (1000 - 100) + 100));
    $("#num-ratings").html("&nbsp" + num + " ratings");
}