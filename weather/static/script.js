window.addEventListener("load", () => {
    // Récupérer l'heure actuelle
    const hour = new Date().getHours();

    // Définir les images de fond en fonction de l'heure
    let backgroundUrl = "";

    // Appliquer des conditions basées sur l'heure
    if (hour >= 6 && hour < 12) {
        // Matin
        backgroundUrl = "url('./image/photo2.png')";
    } else if (hour >= 12 && hour < 18) {
        // Après-midi
        backgroundUrl = "url('./image/photo3.png')";
    } 
    else if (hour >= 18 && hour < 21) {
        // Soir
        backgroundUrl = "url('./image/photo1.png')";
    } else {
        // Nuit
        backgroundUrl = "url('./image/photo5.png')";
    }

    // Appliquer l'image de fond au body de la page
    document.body.style.backgroundImage = backgroundUrl;
    document.body.style.backgroundSize = "cover";
    document.body.style.backgroundPosition = "center";
    document.body.style.height = "100vh"; // S'assurer que le fond couvre toute la page
    document.body.style.margin = "0"; // Enlever les marges par défaut
    document.body.style.padding = "0"; // Enlever les marges intérieures par défaut
});
