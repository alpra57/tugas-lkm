addHeart() {
    this.heartMaterial = new THREE.ShaderMaterial({
        fragmentShader: document.getElementById("fragmentShader").textContent,
        vertexShader: document.getElementById("vertexShader").textContent,
        uniforms: {
            uTime: { value: 0 },
            uSize: { value: 0.2},
            uTEX: {
                value: new THREE.TextureLoader().load(
                    "https://assets.codepen.io/74321/heart.png"
                )
            }
    });
}