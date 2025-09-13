console.clear();

/* SETUP */
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  5000
);
camera.position.z = 500;

const renderer = new THREE.WebGLRenderer();
renderer.setPixelRatio(window.devicePixelRatio > 1 ? 2 : 1);
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const controlsWebGL = new THREE.OrbitControls(camera, renderer.domElement);

/* HEART PARTICLES */
const tl = gsap.timeline({ repeat: -1, yoyo: true });

const path = document.querySelector("path");
const length = path.getTotalLength();
const vertices = [];

for (let i = 0; i < length; i += 0.1) {
  const point = path.getPointAtLength(i);
  const vector = new THREE.Vector3(point.x, -point.y, 0);

  vector.x += (Math.random() - 0.5) * 30;
  vector.y += (Math.random() - 0.5) * 30;
  vector.z += (Math.random() - 0.5) * 70;

  vertices.push(vector);

  tl.from(vector, {
      x: 600 / 2,
      y: -552 / 2,
      z: 0,
      ease: "power2.inOut",
      duration: "random(2, 5)"
    },
    i * 0.002
  );
}

const geometry = new THREE.BufferGeometry().setFromPoints(vertices);
const material = new THREE.PointsMaterial({
  color: 0xee5282,
  blending: THREE.AdditiveBlending,
  size: 3,
  transparent: true,
  opacity: 1
});

const particles = new THREE.Points(geometry, material);
particles.position.x -= 600 / 2;
particles.position.y += 552 / 2;
scene.add(particles);

/* INTRO ANIMATION */
gsap.from(particles.position, { z: -1000, duration: 2.5, ease: "power4.out" });
gsap.from(particles.material, { opacity: 0, duration: 2, ease: "sine.inOut" });

/* ROTATION */
gsap.fromTo(scene.rotation, { y: -0.2 }, {
  y: 0.2,
  repeat: -1,
  yoyo: true,
  ease: 'power2.inOut',
  duration: 3
});

/* ✨ NAME PARTICLES (Ananya) - FIXED VERSION */
const loader = new THREE.FontLoader();
loader.load('https://threejs.org/examples/fonts/helvetiker_regular.typeface.json', function (font) {
  
  // Generate shapes from the font (this gives us the 2D shapes of each letter)
  const shapes = font.generateShapes("Ananya", 50);
  
  // Calculate overall bounding box for centering
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  for (let s = 0; s < shapes.length; s++) {
    const shape = shapes[s];
    const points = shape.getPoints(20);
    for (let p = 0; p < points.length; p++) {
      minX = Math.min(minX, points[p].x);
      minY = Math.min(minY, points[p].y);
      maxX = Math.max(maxX, points[p].x);
      maxY = Math.max(maxY, points[p].y);
    }
  }
  
  const centerOffsetX = -(maxX + minX) / 2;
  const centerOffsetY = -(maxY + minY) / 2;
  
  // Sample points within each letter shape (not just the outline)
  const nameVertices = [];
  const totalPoints = 8000; // Total points to create solid text
  
  for (let s = 0; s < shapes.length; s++) {
    const shape = shapes[s];
    const points = shape.getPoints(50); // Get detailed boundary points
    
    // Create bounding box for this shape
    let shapeMinX = Infinity, shapeMinY = Infinity, shapeMaxX = -Infinity, shapeMaxY = -Infinity;
    for (let p = 0; p < points.length; p++) {
      shapeMinX = Math.min(shapeMinX, points[p].x);
      shapeMinY = Math.min(shapeMinY, points[p].y);
      shapeMaxX = Math.max(shapeMaxX, points[p].x);
      shapeMaxY = Math.max(shapeMaxY, points[p].y);
    }
    
    // Sample random points within the letter shape using ray casting
    const pointsPerShape = totalPoints / shapes.length;
    for (let i = 0; i < pointsPerShape; i++) {
      const x = shapeMinX + Math.random() * (shapeMaxX - shapeMinX);
      const y = shapeMinY + Math.random() * (shapeMaxY - shapeMinY);
      
      // Ray casting algorithm to check if point is inside the shape
      let inside = false;
      for (let p = 0, j = points.length - 1; p < points.length; j = p++) {
        const xi = points[p].x, yi = points[p].y;
        const xj = points[j].x, yj = points[j].y;
        
        const intersect = ((yi > y) !== (yj > y)) && 
                          (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
        if (intersect) inside = !inside;
      }
      
      if (inside) {
        const vector = new THREE.Vector3(
          x + centerOffsetX,
          y + centerOffsetY,
          (Math.random() - 0.5) * 3
        );
        nameVertices.push(vector);
      }
    }
  }
  
  const nameGeometry = new THREE.BufferGeometry().setFromPoints(nameVertices);
  const nameMaterial = new THREE.PointsMaterial({
    color: 0xffffff,
    size: 2.2,
    transparent: true,
    opacity: 1
  });

  const nameParticles = new THREE.Points(nameGeometry, nameMaterial);

  // Position in the heart
  nameParticles.position.x = 0;
  nameParticles.position.y = 0;
  nameParticles.position.z = 0;

  scene.add(nameParticles);

  // Animate text
  gsap.from(nameParticles.position, {
    z: -800,
    duration: 2,
    ease: "power4.out",
    delay: 1.2
  });
  gsap.from(nameParticles.material, {
    opacity: 0,
    duration: 1.5,
    delay: 1.2,
    ease: "sine.inOut"
  });
});

/* RENDERING */
function render() {
  requestAnimationFrame(render);
  geometry.setFromPoints(vertices);
  renderer.render(scene, camera);
}

/* EVENTS */
function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}
window.addEventListener("resize", onWindowResize, false);

requestAnimationFrame(render);