function printDonut(radiusOuter, radiusInner) {
    // Create a square grid of size (2*radiusOuter + 1)
    const size = 2 * radiusOuter + 1;
    const center = radiusOuter;

    let result = "";

    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            // Calculate the distance from the center
            const distance = Math.sqrt((i - center) ** 2 + (j - center) ** 2);

            // Append * if the distance is between the inner and outer radius
            if (radiusInner < distance && distance < radiusOuter) {
                result += "*";
            } else {
                result += " ";
            }
        }
        result += "\n";
    }

    console.log(result);
}


printDonut(50, 30);
