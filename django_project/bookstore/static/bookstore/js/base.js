document.getElementById("search-button").onclick = null;

// Check if search bar is being used outside of the filters
document.getElementById("search-button").onclick = (event) => {
    if ($("title").html().includes("Explore")) {
        event.preventDefault();
        $("#category-filtered").val($("#search-select").val());
        $("#input-filtered").val($("#input").val());
        $("#filtered-query").submit();
    }
    else {
        event.preventDefault();
        $("#query").submit();
    }
}


