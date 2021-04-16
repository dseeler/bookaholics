window.onload = (event) => {
    // Add rating stars
    const rating = $("#book-rating").html();
    for (let i = 0; i <= rating; i++){
        $("#star" + i).addClass("checked");
    }

    // Add random number of ratings
    const num = Math.floor((Math.random() * (1000 - 100) + 100));
    $("#num-ratings").html("&nbsp" + num + " ratings");

    // Add random page count
    const count = Math.floor((Math.random() * (500 - 300) + 300));
    $("#page-count").html(count);

    // Add random weight
    const weight = Math.floor((Math.random() * (9 - 7) + 7));
    $("#shipping-weight").html("0." + weight + " pounds");

    const originalPrice = $("#original-price").val();

    $("#quantity").change(() => {
        $("#price").html("<b>$" + ($("#quantity").val() * originalPrice)  + "</b>");
    });
}

