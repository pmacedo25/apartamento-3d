// HI VIEW ALTO DA BOA VISTA - 3D INTERACTIVE ARCHITECTURAL VIEWER
// Proportions extracted 1:1 from Official Blueprint (Scale 1:75, 125.79 m²)

let scene, camera, renderer, orbitControls;
let currentMode = 'orbit'; // 'orbit', 'fps', 'plan'
let apartmentGroup, wallsGroup, floorsGroup, labelsGroup, ceilingGroup, doorsGroup;
let floorPlanMesh = null;
let measurePoints = [];
let measureLine = null;
let isMeasuring = false;

// First Person State
const player = {
    pos: new THREE.Vector3(7.20, 1.68, 4.50), // Start in Living Room
    rotY: -Math.PI / 2, // Looking toward terrace
    pitch: 0,
    speed: 3.5,
    radius: 0.32,
    height: 1.68
};
const keys = { w: false, a: false, s: false, d: false, shift: false };
let isPointerLocked = false;
let isDraggingFPS = false;
let prevMousePos = { x: 0, y: 0 };
let currentRoom = null;

// Clock
const clock = new THREE.Clock();

// Textures cache
const textures = {};

function init() {
    const container = document.getElementById('viewport-container');
    
    // Scene
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x181a1e);
    scene.fog = new THREE.FogExp2(0x181a1e, 0.015);

    // Camera
    camera = new THREE.PerspectiveCamera(65, window.innerWidth / window.innerHeight, 0.1, 150);
    
    // Renderer
    renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.05;
    container.appendChild(renderer.domElement);

    // Orbit Controls
    orbitControls = new THREE.OrbitControls(camera, renderer.domElement);
    orbitControls.enableDamping = true;
    orbitControls.dampingFactor = 0.08;
    orbitControls.maxPolarAngle = Math.PI / 2 - 0.02; // Don't go below ground
    orbitControls.minDistance = 2;
    orbitControls.maxDistance = 50;

    // Groups
    apartmentGroup = new THREE.Group();
    wallsGroup = new THREE.Group();
    floorsGroup = new THREE.Group();
    labelsGroup = new THREE.Group();
    ceilingGroup = new THREE.Group();
    doorsGroup = new THREE.Group();

    apartmentGroup.add(floorsGroup);
    apartmentGroup.add(wallsGroup);
    apartmentGroup.add(doorsGroup);
    apartmentGroup.add(ceilingGroup);
    apartmentGroup.add(labelsGroup);
    scene.add(apartmentGroup);

    // Center apartment in the world
    // Apartment bounds: X [0.4, 13.35], Z [0.44, 11.0] -> Center roughly at (6.87, 0, 5.72)
    apartmentGroup.position.set(-6.87, 0, -5.72);

    // Generate Procedural Textures
    initTextures();

    // Setup Lighting
    setupLighting('day');

    // Build Architectural Geometry
    buildFloors();
    buildWalls();
    buildFloorPlanOverlay();
    buildRoomLabels();

    // Setup Camera Mode
    setMode('orbit');

    // Setup Event Listeners
    setupEvents();

    // Minimap
    initMinimap();

    // Animation Loop
    animate();
}

// Procedural Canvas Textures for PBR
function initTextures() {
    // 1. Porcelain Tile 90x90cm (Living / Kitchen)
    const cvPorcelain = document.createElement('canvas');
    cvPorcelain.width = 512; cvPorcelain.height = 512;
    const ctxP = cvPorcelain.getContext('2d');
    ctxP.fillStyle = '#f0ede6';
    ctxP.fillRect(0, 0, 512, 512);
    ctxP.strokeStyle = '#d5d0c5';
    ctxP.lineWidth = 4;
    ctxP.strokeRect(0, 0, 512, 512);
    // Subtle noise
    for (let i = 0; i < 4000; i++) {
        ctxP.fillStyle = Math.random() > 0.5 ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.03)';
        ctxP.fillRect(Math.random() * 512, Math.random() * 512, 2, 2);
    }
    const texPorcelain = new THREE.CanvasTexture(cvPorcelain);
    texPorcelain.wrapS = THREE.RepeatWrapping;
    texPorcelain.wrapT = THREE.RepeatWrapping;
    texPorcelain.repeat.set(1.1, 1.1);
    textures.porcelain = texPorcelain;

    // 2. Wood Laminate Planks (Suites)
    const cvWood = document.createElement('canvas');
    cvWood.width = 512; cvWood.height = 512;
    const ctxW = cvWood.getContext('2d');
    ctxW.fillStyle = '#c5a882';
    ctxW.fillRect(0, 0, 512, 512);
    // Planks
    for (let y = 0; y < 512; y += 64) {
        ctxW.strokeStyle = '#9e805b';
        ctxW.lineWidth = 2;
        ctxW.beginPath(); ctxW.moveTo(0, y); ctxW.lineTo(512, y); ctxW.stroke();
        // random grain lines
        for (let j = 0; j < 30; j++) {
            ctxW.fillStyle = 'rgba(120, 85, 50, 0.08)';
            ctxW.fillRect(Math.random() * 512, y + Math.random() * 60, Math.random() * 80 + 20, 1.5);
        }
    }
    const texWood = new THREE.CanvasTexture(cvWood);
    texWood.wrapS = THREE.RepeatWrapping;
    texWood.wrapT = THREE.RepeatWrapping;
    texWood.repeat.set(1.5, 1.5);
    textures.wood = texWood;

    // 3. Terrace Outdoor Tile (Gourmet)
    const cvTerrace = document.createElement('canvas');
    cvTerrace.width = 512; cvTerrace.height = 512;
    const ctxT = cvTerrace.getContext('2d');
    ctxT.fillStyle = '#b8af9e';
    ctxT.fillRect(0, 0, 512, 512);
    ctxT.strokeStyle = '#8f8574';
    ctxT.lineWidth = 3;
    ctxT.strokeRect(0, 0, 512, 512);
    const texTerrace = new THREE.CanvasTexture(cvTerrace);
    texTerrace.wrapS = THREE.RepeatWrapping;
    texTerrace.wrapT = THREE.RepeatWrapping;
    texTerrace.repeat.set(1.5, 1.5);
    textures.terrace = texTerrace;

    // 4. Bath Tile / Grey Ceramic
    const cvBath = document.createElement('canvas');
    cvBath.width = 256; cvBath.height = 256;
    const ctxB = cvBath.getContext('2d');
    ctxB.fillStyle = '#dedad2';
    ctxB.fillRect(0, 0, 256, 256);
    ctxB.strokeStyle = '#bbb6ad';
    ctxB.lineWidth = 3;
    ctxB.strokeRect(0, 0, 256, 256);
    const texBath = new THREE.CanvasTexture(cvBath);
    texBath.wrapS = THREE.RepeatWrapping;
    texBath.wrapT = THREE.RepeatWrapping;
    texBath.repeat.set(2, 2);
    textures.bath = texBath;
}

// Lighting Setup
let dirLight, hemiLight, ceilingLights = [];
function setupLighting(preset = 'day') {
    if (dirLight) scene.remove(dirLight);
    if (hemiLight) scene.remove(hemiLight);
    ceilingLights.forEach(l => scene.remove(l));
    ceilingLights = [];

    if (preset === 'day') {
        // Natural Sun from West / Balcony
        hemiLight = new THREE.HemisphereLight(0xfff8ee, 0x3d434d, 0.75);
        scene.add(hemiLight);

        dirLight = new THREE.DirectionalLight(0xfffaed, 1.25);
        dirLight.position.set(-15, 18, 5); // Angle from West/Terrace
        dirLight.castShadow = true;
        dirLight.shadow.mapSize.width = 2048;
        dirLight.shadow.mapSize.height = 2048;
        dirLight.shadow.camera.near = 0.5;
        dirLight.shadow.camera.far = 50;
        dirLight.shadow.camera.left = -12;
        dirLight.shadow.camera.right = 12;
        dirLight.shadow.camera.top = 12;
        dirLight.shadow.camera.bottom = -12;
        dirLight.shadow.bias = -0.0004;
        scene.add(dirLight);
        scene.background = new THREE.Color(0x181a1e);
    } else if (preset === 'sunset') {
        hemiLight = new THREE.HemisphereLight(0xffd4aa, 0x2d2f3b, 0.65);
        scene.add(hemiLight);

        dirLight = new THREE.DirectionalLight(0xff9944, 1.4);
        dirLight.position.set(-20, 6, 8);
        dirLight.castShadow = true;
        dirLight.shadow.mapSize.width = 2048;
        dirLight.shadow.mapSize.height = 2048;
        dirLight.shadow.bias = -0.0004;
        scene.add(dirLight);
        scene.background = new THREE.Color(0x15121c);
    } else if (preset === 'night') {
        hemiLight = new THREE.HemisphereLight(0x222633, 0x0d0f14, 0.25);
        scene.add(hemiLight);

        // Ceiling downlights in rooms (as per electrical plan)
        APARTMENT_DATA.rooms.forEach(room => {
            const cx = (room.box[0] + room.box[2]) / 2 - 6.87;
            const cz = (room.box[1] + room.box[3]) / 2 - 5.72;
            const light = new THREE.PointLight(0xffecd0, 0.85, 6);
            light.position.set(cx, 2.55, cz);
            light.castShadow = false;
            scene.add(light);
            ceilingLights.push(light);

            // Small glowing spot mesh
            const spotGeo = new THREE.SphereGeometry(0.06, 8, 8);
            const spotMat = new THREE.MeshBasicMaterial({ color: 0xffeedd });
            const spotMesh = new THREE.Mesh(spotGeo, spotMat);
            spotMesh.position.copy(light.position);
            scene.add(spotMesh);
            ceilingLights.push(spotMesh);
        });
        scene.background = new THREE.Color(0x0c0d12);
    }
}

// Build Floors for each room
function buildFloors() {
    APARTMENT_DATA.rooms.forEach(room => {
        const x1 = room.box[0];
        const z1 = room.box[1];
        const x2 = room.box[2];
        const z2 = room.box[3];
        const w = x2 - x1;
        const d = z2 - z1;
        const cx = x1 + w / 2;
        const cz = z1 + d / 2;

        let floorTex = textures.porcelain;
        let roughness = 0.35;
        let metalness = 0.05;

        if (room.floor === 'wood') {
            floorTex = textures.wood;
            roughness = 0.5;
        } else if (room.floor === 'deck_or_tile') {
            floorTex = textures.terrace;
            roughness = 0.6;
        } else if (room.floor === 'tile_light' || room.floor === 'tile_dark' || room.floor === 'marble') {
            floorTex = textures.bath;
            roughness = 0.3;
        } else if (room.floor === 'concrete') {
            floorTex = textures.bath;
            roughness = 0.8;
        }

        const floorMat = new THREE.MeshStandardMaterial({
            map: floorTex,
            roughness: roughness,
            metalness: metalness
        });

        const floorGeo = new THREE.PlaneGeometry(w, d);
        const floorMesh = new THREE.Mesh(floorGeo, floorMat);
        floorMesh.rotation.x = -Math.PI / 2;
        floorMesh.position.set(cx, 0.001, cz);
        floorMesh.receiveShadow = true;
        floorMesh.userData = { room: room };
        floorsGroup.add(floorMesh);

        // Ceiling (removable)
        const ceilGeo = new THREE.PlaneGeometry(w, d);
        const ceilMat = new THREE.MeshStandardMaterial({
            color: 0xfdfdfd,
            roughness: 0.9,
            side: THREE.DoubleSide
        });
        const ceilMesh = new THREE.Mesh(ceilGeo, ceilMat);
        ceilMesh.rotation.x = Math.PI / 2;
        ceilMesh.position.set(cx, 2.70, cz);
        ceilMesh.receiveShadow = true;
        ceilingGroup.add(ceilMesh);
    });

    // Base ground slab underneath apartment
    const slabGeo = new THREE.BoxGeometry(15, 0.2, 13);
    const slabMat = new THREE.MeshStandardMaterial({ color: 0x22242a, roughness: 0.9 });
    const slabMesh = new THREE.Mesh(slabGeo, slabMat);
    slabMesh.position.set(6.87, -0.1, 5.72);
    slabMesh.receiveShadow = true;
    floorsGroup.add(slabMesh);
}

// Build Walls with Openings
const wallMaterial = new THREE.MeshStandardMaterial({
    color: 0xf2efe9,
    roughness: 0.7,
    metalness: 0.02
});
const baseboardMaterial = new THREE.MeshStandardMaterial({
    color: 0xffffff,
    roughness: 0.4
});
const glassMaterial = new THREE.MeshPhysicalMaterial({
    color: 0x99bbcc,
    transparent: true,
    opacity: 0.28,
    roughness: 0.05,
    metalness: 0.1,
    transmission: 0.9,
    ior: 1.5,
    side: THREE.DoubleSide
});
const frameMaterial = new THREE.MeshStandardMaterial({
    color: 0x232528,
    roughness: 0.4,
    metalness: 0.6
});
const doorWoodMaterial = new THREE.MeshStandardMaterial({
    color: 0xd9cbb8,
    roughness: 0.5,
    metalness: 0.05
});

function buildWalls() {
    APARTMENT_DATA.walls.forEach(w => {
        const dx = w.x2 - w.x1;
        const dz = w.z2 - w.z1;
        const len = Math.hypot(dx, dz);
        if (len < 0.05) return;

        const angle = Math.atan2(dz, dx);
        const wallHeight = w.height || 2.70;
        const thick = w.thick || 0.15;

        // Wall Container
        const wallObj = new THREE.Group();
        wallObj.position.set(w.x1, 0, w.z1);
        wallObj.rotation.y = -angle; // Three.js Y rotation
        wallObj.userData = { wallData: w, baseHeight: wallHeight };

        if (w.type === 'railing') {
            // Balcony Glass Railing h = 1.20m
            buildBalconyRailing(wallObj, len, 1.20, thick);
            wallsGroup.add(wallObj);
            return;
        }

        if (w.type === 'countertop') {
            // Kitchen American Counter h = 0.92m
            const topGeo = new THREE.BoxGeometry(len, 0.92, thick);
            const topMat = new THREE.MeshStandardMaterial({ color: 0x2a2b2e, roughness: 0.25, metalness: 0.1 });
            const topMesh = new THREE.Mesh(topGeo, topMat);
            topMesh.position.set(len / 2, 0.46, 0);
            topMesh.castShadow = true; topMesh.receiveShadow = true;
            wallObj.add(topMesh);
            wallsGroup.add(wallObj);
            return;
        }

        if (w.type === 'sliding_glass_wall') {
            // Large Living Room / Balcony Glass Sliding Doors (4.2m x 2.45m)
            buildSlidingGlassWall(wallObj, len, wallHeight, thick);
            wallsGroup.add(wallObj);
            return;
        }

        // Standard wall with doors/windows
        if (!w.openings || w.openings.length === 0) {
            // Solid Wall
            const solidGeo = new THREE.BoxGeometry(len, wallHeight, thick);
            const solidMesh = new THREE.Mesh(solidGeo, wallMaterial);
            solidMesh.position.set(len / 2, wallHeight / 2, 0);
            solidMesh.castShadow = true; solidMesh.receiveShadow = true;
            wallObj.add(solidMesh);

            // Baseboard
            const bbGeo = new THREE.BoxGeometry(len, 0.14, thick + 0.02);
            const bbMesh = new THREE.Mesh(bbGeo, baseboardMaterial);
            bbMesh.position.set(len / 2, 0.07, 0);
            wallObj.add(bbMesh);
        } else {
            // Wall with openings
            let currentX = 0;
            w.openings.sort((a, b) => a.start - b.start);

            w.openings.forEach((op, idx) => {
                const opStart = Math.max(0, op.start);
                const opEnd = Math.min(len, opStart + op.width);
                const segLen = opStart - currentX;

                // 1. Solid segment before opening
                if (segLen > 0.02) {
                    const segGeo = new THREE.BoxGeometry(segLen, wallHeight, thick);
                    const segMesh = new THREE.Mesh(segGeo, wallMaterial);
                    segMesh.position.set(currentX + segLen / 2, wallHeight / 2, 0);
                    segMesh.castShadow = true; segMesh.receiveShadow = true;
                    wallObj.add(segMesh);

                    // Baseboard
                    const bbGeo = new THREE.BoxGeometry(segLen, 0.14, thick + 0.02);
                    const bbMesh = new THREE.Mesh(bbGeo, baseboardMaterial);
                    bbMesh.position.set(currentX + segLen / 2, 0.07, 0);
                    wallObj.add(bbMesh);
                }

                const opW = opEnd - opStart;

                if (op.type === 'door' || op.type === 'opening') {
                    const dh = op.height || 2.10;
                    // Lintel (segment above door up to ceiling)
                    const lintelH = wallHeight - dh;
                    if (lintelH > 0.02) {
                        const lintelGeo = new THREE.BoxGeometry(opW, lintelH, thick);
                        const lintelMesh = new THREE.Mesh(lintelGeo, wallMaterial);
                        lintelMesh.position.set(opStart + opW / 2, dh + lintelH / 2, 0);
                        lintelMesh.castShadow = true; lintelMesh.receiveShadow = true;
                        wallObj.add(lintelMesh);
                    }

                    if (op.type === 'door') {
                        // Door Frame
                        buildDoorFrameAndLeaf(wallObj, opStart, opW, dh, thick);
                    }
                } else if (op.type === 'window' || op.type === 'ventilation') {
                    const sill = op.sill || 0.90;
                    const wh = op.height || 1.30;
                    // Sill wall (under window)
                    if (sill > 0.02) {
                        const sillGeo = new THREE.BoxGeometry(opW, sill, thick);
                        const sillMesh = new THREE.Mesh(sillGeo, wallMaterial);
                        sillMesh.position.set(opStart + opW / 2, sill / 2, 0);
                        sillMesh.castShadow = true; sillMesh.receiveShadow = true;
                        wallObj.add(sillMesh);

                        // Baseboard under sill
                        const bbGeo = new THREE.BoxGeometry(opW, 0.14, thick + 0.02);
                        const bbMesh = new THREE.Mesh(bbGeo, baseboardMaterial);
                        bbMesh.position.set(opStart + opW / 2, 0.07, 0);
                        wallObj.add(bbMesh);
                    }

                    // Lintel wall (above window)
                    const topY = sill + wh;
                    const lintelH = wallHeight - topY;
                    if (lintelH > 0.02) {
                        const lintelGeo = new THREE.BoxGeometry(opW, lintelH, thick);
                        const lintelMesh = new THREE.Mesh(lintelGeo, wallMaterial);
                        lintelMesh.position.set(opStart + opW / 2, topY + lintelH / 2, 0);
                        lintelMesh.castShadow = true; lintelMesh.receiveShadow = true;
                        wallObj.add(lintelMesh);
                    }

                    // Window Frame & Glass
                    buildWindowFrameAndGlass(wallObj, opStart, opW, sill, wh, thick);
                }

                currentX = opEnd;
            });

            // Segment after last opening
            const remLen = len - currentX;
            if (remLen > 0.02) {
                const segGeo = new THREE.BoxGeometry(remLen, wallHeight, thick);
                const segMesh = new THREE.Mesh(segGeo, wallMaterial);
                segMesh.position.set(currentX + remLen / 2, wallHeight / 2, 0);
                segMesh.castShadow = true; segMesh.receiveShadow = true;
                wallObj.add(segMesh);

                const bbGeo = new THREE.BoxGeometry(remLen, 0.14, thick + 0.02);
                const bbMesh = new THREE.Mesh(bbGeo, baseboardMaterial);
                bbMesh.position.set(currentX + remLen / 2, 0.07, 0);
                wallObj.add(bbMesh);
            }
        }

        wallsGroup.add(wallObj);
    });
}

// Build Balcony Railing (Guarda-corpo h=1.20m)
function buildBalconyRailing(group, len, h, thick) {
    // Glass panel
    const glassGeo = new THREE.BoxGeometry(len, h - 0.10, 0.02);
    const glassMesh = new THREE.Mesh(glassGeo, glassMaterial);
    glassMesh.position.set(len / 2, h / 2, 0);
    group.add(glassMesh);

    // Top Handrail
    const railGeo = new THREE.BoxGeometry(len, 0.06, 0.08);
    const railMesh = new THREE.Mesh(railGeo, frameMaterial);
    railMesh.position.set(len / 2, h - 0.03, 0);
    group.add(railMesh);

    // Bottom Base
    const baseGeo = new THREE.BoxGeometry(len, 0.08, thick);
    const baseMesh = new THREE.Mesh(baseGeo, wallMaterial);
    baseMesh.position.set(len / 2, 0.04, 0);
    group.add(baseMesh);

    // Posts every ~1.2m
    const numPosts = Math.max(2, Math.round(len / 1.2));
    for (let i = 0; i <= numPosts; i++) {
        const px = (len / numPosts) * i;
        const postGeo = new THREE.BoxGeometry(0.04, h, 0.04);
        const postMesh = new THREE.Mesh(postGeo, frameMaterial);
        postMesh.position.set(px, h / 2, 0);
        group.add(postMesh);
    }
}

// Build Sliding Glass Wall (Living Room <-> Terrace)
function buildSlidingGlassWall(group, len, h, thick) {
    const doorH = 2.45;
    const lintelH = h - doorH;

    // Lintel above glass
    if (lintelH > 0.02) {
        const topGeo = new THREE.BoxGeometry(len, lintelH, thick);
        const topMesh = new THREE.Mesh(topGeo, wallMaterial);
        topMesh.position.set(len / 2, doorH + lintelH / 2, 0);
        topMesh.castShadow = true;
        group.add(topMesh);
    }

    // 4 Sliding Panels (Black Aluminum Frames + Clear Glass)
    const panelW = len / 4;
    for (let i = 0; i < 4; i++) {
        const px = panelW * i + panelW / 2;
        const pz = (i % 2 === 0 ? 0.03 : -0.03);

        // Frame
        const fGeo = new THREE.BoxGeometry(panelW - 0.04, doorH, 0.04);
        // Glass
        const gGeo = new THREE.BoxGeometry(panelW - 0.12, doorH - 0.12, 0.015);
        const gMesh = new THREE.Mesh(gGeo, glassMaterial);
        gMesh.position.set(px, doorH / 2, pz);
        group.add(gMesh);

        // Perimeter frame lines
        const frameMesh = new THREE.Mesh(fGeo, frameMaterial);
        frameMesh.position.set(px, doorH / 2, pz);
        // wireframe box or hollow frame
        group.add(frameMesh);
    }
}

// Build Door Frame and Leaf (Semi-Open)
function buildDoorFrameAndLeaf(group, start, w, h, thick) {
    const frameThick = 0.04;
    // Left post
    const leftPostGeo = new THREE.BoxGeometry(frameThick, h, thick + 0.01);
    const leftPost = new THREE.Mesh(leftPostGeo, frameMaterial);
    leftPost.position.set(start + frameThick / 2, h / 2, 0);
    group.add(leftPost);

    // Right post
    const rightPostGeo = new THREE.BoxGeometry(frameThick, h, thick + 0.01);
    const rightPost = new THREE.Mesh(rightPostGeo, frameMaterial);
    rightPost.position.set(start + w - frameThick / 2, h / 2, 0);
    group.add(rightPost);

    // Header
    const headGeo = new THREE.BoxGeometry(w, frameThick, thick + 0.01);
    const head = new THREE.Mesh(headGeo, frameMaterial);
    head.position.set(start + w / 2, h - frameThick / 2, 0);
    group.add(head);

    // Door Leaf (Ajar at 55 degrees)
    const leafW = w - frameThick * 2;
    const leafGeo = new THREE.BoxGeometry(leafW, h - frameThick, 0.04);
    const leafMesh = new THREE.Mesh(leafGeo, doorWoodMaterial);
    leafMesh.position.set(leafW / 2, (h - frameThick) / 2, 0);
    leafMesh.castShadow = true;

    // Door pivot group at hinge
    const pivot = new THREE.Group();
    pivot.position.set(start + frameThick, 0, 0);
    pivot.rotation.y = Math.PI / 3.2; // ~56 degrees open!
    pivot.add(leafMesh);

    // Door handle (metallic lever)
    const handleGeo = new THREE.BoxGeometry(0.12, 0.03, 0.06);
    const handleMat = new THREE.MeshStandardMaterial({ color: 0xcccccc, metalness: 0.9, roughness: 0.2 });
    const handleMesh = new THREE.Mesh(handleGeo, handleMat);
    handleMesh.position.set(leafW - 0.08, 0.98, 0.03);
    pivot.add(handleMesh);

    doorsGroup.add(pivot);
    group.add(pivot);
}

// Build Window Frame and Glass
function buildWindowFrameAndGlass(group, start, w, sill, h, thick) {
    const frameThick = 0.05;
    const cy = sill + h / 2;
    const cx = start + w / 2;

    // Glass
    const glassGeo = new THREE.BoxGeometry(w - 0.08, h - 0.08, 0.015);
    const glassMesh = new THREE.Mesh(glassGeo, glassMaterial);
    glassMesh.position.set(cx, cy, 0);
    group.add(glassMesh);

    // Frame (Mullions & border)
    const frameGeo = new THREE.BoxGeometry(w, h, thick * 0.7);
    const frameMesh = new THREE.Mesh(frameGeo, frameMaterial);
    frameMesh.position.set(cx, cy, 0);
    group.add(frameMesh);
}

// Overlay Original Floor Plan on Ground
function buildFloorPlanOverlay() {
    if (typeof APARTMENT_PLAN_B64 === 'undefined') return;

    const img = new Image();
    img.src = APARTMENT_PLAN_B64;
    img.onload = () => {
        const tex = new THREE.Texture(img);
        tex.needsUpdate = true;

        // Plane matches exact bounds: 13.494m x 11.377m
        const planeGeo = new THREE.PlaneGeometry(13.494, 11.377);
        const planeMat = new THREE.MeshBasicMaterial({
            map: tex,
            transparent: true,
            opacity: 0.85,
            depthWrite: false
        });
        floorPlanMesh = new THREE.Mesh(planeGeo, planeMat);
        floorPlanMesh.rotation.x = -Math.PI / 2;
        floorPlanMesh.position.set(13.494 / 2, 0.003, 11.377 / 2);
        floorPlanMesh.visible = false; // Toggleable!
        apartmentGroup.add(floorPlanMesh);
    };
}

// 3D Room Name Badges
function buildRoomLabels() {
    APARTMENT_DATA.rooms.forEach(r => {
        const cx = (r.box[0] + r.box[2]) / 2;
        const cz = (r.box[1] + r.box[3]) / 2;

        const canvas = document.createElement('canvas');
        canvas.width = 256; canvas.height = 128;
        const ctx = canvas.getContext('2d');
        ctx.fillStyle = 'rgba(24, 26, 30, 0.82)';
        ctx.roundRect ? ctx.roundRect(4, 4, 248, 120, 16) : ctx.fillRect(4, 4, 248, 120);
        ctx.fill();
        ctx.strokeStyle = '#c5a882';
        ctx.lineWidth = 3;
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 22px Segoe UI, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(r.name, 128, 52);

        ctx.fillStyle = '#c5a882';
        ctx.font = 'bold 20px Consolas, monospace';
        ctx.fillText(`${r.area.toFixed(1)} m²`, 128, 92);

        const tex = new THREE.CanvasTexture(canvas);
        const spriteMat = new THREE.SpriteMaterial({ map: tex, transparent: true });
        const sprite = new THREE.Sprite(spriteMat);
        sprite.position.set(cx, 1.95, cz);
        sprite.scale.set(1.4, 0.7, 1);
        labelsGroup.add(sprite);
    });
}

// Set Camera Mode
function setMode(mode) {
    currentMode = mode;
    document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
    const btn = document.getElementById(`btn-${mode}`);
    if (btn) btn.classList.add('active');

    const fpsHUD = document.getElementById('fps-crosshair');
    const cutControl = document.getElementById('cut-height-control');

    if (mode === 'orbit') {
        orbitControls.enabled = true;
        camera.position.set(0, 14, 16);
        orbitControls.target.set(0, 1.2, 0);
        orbitControls.update();
        if (fpsHUD) fpsHUD.style.display = 'none';
        if (cutControl) cutControl.style.display = 'flex';
        setWallsHeight(document.getElementById('wall-height-slider').value);
    } else if (mode === 'plan') {
        orbitControls.enabled = true;
        camera.position.set(0, 22, 0.001); // Top down
        orbitControls.target.set(0, 0, 0);
        orbitControls.update();
        if (fpsHUD) fpsHUD.style.display = 'none';
        if (cutControl) cutControl.style.display = 'none';
        setWallsHeight(1.2);
    } else if (mode === 'fps') {
        orbitControls.enabled = false;
        camera.position.copy(player.pos).add(apartmentGroup.position);
        updateCameraRotation();
        if (fpsHUD) fpsHUD.style.display = 'block';
        if (cutControl) cutControl.style.display = 'none';
        setWallsHeight(2.70); // Full height walls when inside!
    }
}

// Teleport to Room
function teleportTo(roomId) {
    const room = APARTMENT_DATA.rooms.find(r => r.id === roomId);
    if (!room) return;

    player.pos.set(room.spawn[0], room.spawn[1], room.spawn[2]);
    player.rotY = room.spawn[3];
    player.pitch = 0;

    if (currentMode !== 'fps') {
        setMode('fps');
    } else {
        camera.position.copy(player.pos).add(apartmentGroup.position);
        updateCameraRotation();
    }
    updateCurrentRoomDisplay();
}

// Wall Cut Height
function setWallsHeight(heightVal) {
    const h = parseFloat(heightVal);
    document.getElementById('wall-height-val').innerText = `${h.toFixed(1)}m`;

    wallsGroup.children.forEach(wObj => {
        const baseH = wObj.userData.baseHeight || 2.70;
        const targetScaleY = Math.min(1.0, h / baseH);
        wObj.scale.y = targetScaleY;
    });

    // Toggle ceiling visibility
    ceilingGroup.visible = (h >= 2.65 && document.getElementById('toggle-ceiling').checked);
}

// FPS Camera Look
function updateCameraRotation() {
    const euler = new THREE.Euler(0, 0, 0, 'YXZ');
    euler.x = player.pitch;
    euler.y = player.rotY;
    camera.quaternion.setFromEuler(euler);
}

// Event Listeners
function setupEvents() {
    window.addEventListener('resize', onWindowResize);

    // Keyboard
    window.addEventListener('keydown', (e) => {
        const k = e.key.toLowerCase();
        if (k === 'w' || k === 'arrowup') keys.w = true;
        if (k === 'a' || k === 'arrowleft') keys.a = true;
        if (k === 's' || k === 'arrowdown') keys.s = true;
        if (k === 'd' || k === 'arrowright') keys.d = true;
        if (e.shiftKey) keys.shift = true;

        if (e.key === '1') setMode('fps');
        if (e.key === '2') setMode('orbit');
        if (e.key === '3') setMode('plan');
        if (e.key === 'm') toggleMeasure();
    });

    window.addEventListener('keyup', (e) => {
        const k = e.key.toLowerCase();
        if (k === 'w' || k === 'arrowup') keys.w = false;
        if (k === 'a' || k === 'arrowleft') keys.a = false;
        if (k === 's' || k === 'arrowdown') keys.s = false;
        if (k === 'd' || k === 'arrowright') keys.d = false;
        if (!e.shiftKey) keys.shift = false;
    });

    // Mouse Look for FPS
    const canvas = renderer.domElement;
    canvas.addEventListener('mousedown', (e) => {
        if (currentMode === 'fps') {
            isDraggingFPS = true;
            prevMousePos = { x: e.clientX, y: e.clientY };
            // Optional pointer lock
            if (e.button === 0 && !isMeasuring) {
                canvas.requestPointerLock?.();
            }
        } else if (isMeasuring) {
            handleMeasureClick(e);
        }
    });

    window.addEventListener('mouseup', () => {
        isDraggingFPS = false;
    });

    document.addEventListener('pointerlockchange', () => {
        isPointerLocked = (document.pointerLockElement === canvas);
    });

    window.addEventListener('mousemove', (e) => {
        if (currentMode === 'fps') {
            let movementX = 0;
            let movementY = 0;

            if (isPointerLocked) {
                movementX = e.movementX || 0;
                movementY = e.movementY || 0;
            } else if (isDraggingFPS) {
                movementX = e.clientX - prevMousePos.x;
                movementY = e.clientY - prevMousePos.y;
                prevMousePos = { x: e.clientX, y: e.clientY };
            }

            if (movementX !== 0 || movementY !== 0) {
                const sensitivity = 0.0024;
                player.rotY -= movementX * sensitivity;
                player.pitch -= movementY * sensitivity;
                player.pitch = Math.max(-Math.PI / 2.3, Math.min(Math.PI / 2.3, player.pitch));
                updateCameraRotation();
            }
        }
    });

    // Touch Support for Mobile / Tablet
    setupTouchControls();
}

// Touch / Mobile Controls
function setupTouchControls() {
    const touchArea = renderer.domElement;
    let touchStartPos = { x: 0, y: 0 };
    let isTouching = false;

    touchArea.addEventListener('touchstart', (e) => {
        if (currentMode === 'fps' && e.touches.length === 1) {
            isTouching = true;
            touchStartPos = { x: e.touches[0].clientX, y: e.touches[0].clientY };
        }
    }, { passive: true });

    touchArea.addEventListener('touchmove', (e) => {
        if (currentMode === 'fps' && isTouching && e.touches.length === 1) {
            const dx = e.touches[0].clientX - touchStartPos.x;
            const dy = e.touches[0].clientY - touchStartPos.y;
            touchStartPos = { x: e.touches[0].clientX, y: e.touches[0].clientY };

            const sensitivity = 0.004;
            player.rotY -= dx * sensitivity;
            player.pitch -= dy * sensitivity;
            player.pitch = Math.max(-Math.PI / 2.3, Math.min(Math.PI / 2.3, player.pitch));
            updateCameraRotation();
        }
    }, { passive: true });

    touchArea.addEventListener('touchend', () => {
        isTouching = false;
    });
}

// Window Resize
function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

// First Person Movement with Wall Collision
function updateFPSMovement(dt) {
    if (currentMode !== 'fps') return;

    let moveX = 0;
    let moveZ = 0;

    if (keys.w) moveZ -= 1;
    if (keys.s) moveZ += 1;
    if (keys.a) moveX -= 1;
    if (keys.d) moveX += 1;

    if (moveX !== 0 || moveZ !== 0) {
        const len = Math.hypot(moveX, moveZ);
        moveX /= len;
        moveZ /= len;

        const currentSpeed = keys.shift ? player.speed * 1.6 : player.speed;
        const forward = new THREE.Vector3(0, 0, -1).applyAxisAngle(new THREE.Vector3(0, 1, 0), player.rotY);
        const right = new THREE.Vector3(1, 0, 0).applyAxisAngle(new THREE.Vector3(0, 1, 0), player.rotY);

        const deltaMove = new THREE.Vector3()
            .addScaledVector(forward, -moveZ * currentSpeed * dt)
            .addScaledVector(right, moveX * currentSpeed * dt);

        // Tentative new position
        const targetX = player.pos.x + deltaMove.x;
        const targetZ = player.pos.z + deltaMove.z;

        // Collision Check with Apartment Perimeter [0.4 to 13.35, 0.44 to 11.0]
        const boundedX = Math.max(0.60, Math.min(13.15, targetX));
        const boundedZ = Math.max(0.60, Math.min(10.80, targetZ));

        player.pos.x = boundedX;
        player.pos.z = boundedZ;

        camera.position.copy(player.pos).add(apartmentGroup.position);
        updateCurrentRoomDisplay();
    }
}

// Room detection based on coordinates
function updateCurrentRoomDisplay() {
    const px = player.pos.x;
    const pz = player.pos.z;

    let found = null;
    for (const r of APARTMENT_DATA.rooms) {
        if (px >= r.box[0] && px <= r.box[2] && pz >= r.box[1] && pz <= r.box[3]) {
            found = r;
            break;
        }
    }

    if (found && found !== currentRoom) {
        currentRoom = found;
        const badge = document.getElementById('current-room-badge');
        if (badge) {
            badge.innerHTML = `📍 <b>${found.name}</b> <span style="opacity:0.75">(${found.area.toFixed(1)} m²)</span>`;
        }
    }
}

// 2D Minimap
let minimapCanvas, minimapCtx;
function initMinimap() {
    minimapCanvas = document.getElementById('minimap-canvas');
    if (!minimapCanvas) return;
    minimapCtx = minimapCanvas.getContext('2d');

    // Click on minimap to teleport
    minimapCanvas.addEventListener('click', (e) => {
        const rect = minimapCanvas.getBoundingClientRect();
        const mx = e.clientX - rect.left;
        const my = e.clientY - rect.top;

        // Scale: canvas is 180x150, apartment is 14m x 12m
        const aptX = (mx / minimapCanvas.width) * 14.0;
        const aptZ = (my / minimapCanvas.height) * 12.0;

        player.pos.set(aptX, player.height, aptZ);
        if (currentMode !== 'fps') setMode('fps');
        else camera.position.copy(player.pos).add(apartmentGroup.position);
    });
}

function renderMinimap() {
    if (!minimapCtx) return;
    const ctx = minimapCtx;
    const w = minimapCanvas.width;
    const h = minimapCanvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#1c1e24';
    ctx.fillRect(0, 0, w, h);

    const scaleX = w / 14.0;
    const scaleY = h / 12.0;

    // Draw rooms
    APARTMENT_DATA.rooms.forEach(r => {
        const rx = r.box[0] * scaleX;
        const rz = r.box[1] * scaleY;
        const rw = (r.box[2] - r.box[0]) * scaleX;
        const rh = (r.box[3] - r.box[1]) * scaleY;

        ctx.fillStyle = (currentRoom && currentRoom.id === r.id) ? '#384d3b' : '#282b34';
        ctx.fillRect(rx, rz, rw, rh);
        ctx.strokeStyle = '#3d4352';
        ctx.lineWidth = 1;
        ctx.strokeRect(rx, rz, rw, rh);
    });

    // Draw player position & FOV cone
    const px = player.pos.x * scaleX;
    const pz = player.pos.z * scaleY;

    // FOV cone
    ctx.fillStyle = 'rgba(197, 168, 130, 0.28)';
    ctx.beginPath();
    ctx.moveTo(px, pz);
    const fovAngle = 0.55;
    ctx.arc(px, pz, 22, -player.rotY - Math.PI / 2 - fovAngle, -player.rotY - Math.PI / 2 + fovAngle);
    ctx.closePath();
    ctx.fill();

    // Player dot
    ctx.fillStyle = '#c5a882';
    ctx.beginPath();
    ctx.arc(px, pz, 4.5, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 1.5;
    ctx.stroke();
}

// Measuring Tool (Trena Digital)
function toggleMeasure() {
    isMeasuring = !isMeasuring;
    const btn = document.getElementById('btn-measure');
    if (btn) btn.classList.toggle('active', isMeasuring);

    const info = document.getElementById('measure-info');
    if (info) info.style.display = isMeasuring ? 'block' : 'none';

    if (!isMeasuring) {
        clearMeasure();
    }
}

function handleMeasureClick(e) {
    const mouse = new THREE.Vector2(
        (e.clientX / window.innerWidth) * 2 - 1,
        -(e.clientY / window.innerHeight) * 2 + 1
    );

    const raycaster = new THREE.Raycaster();
    raycaster.setFromCamera(mouse, camera);

    const intersects = raycaster.intersectObjects([...floorsGroup.children, ...wallsGroup.children], true);
    if (intersects.length > 0) {
        const pt = intersects[0].point;
        measurePoints.push(pt);

        // Marker Sphere
        const dotGeo = new THREE.SphereGeometry(0.08, 12, 12);
        const dotMat = new THREE.MeshBasicMaterial({ color: 0xff3344 });
        const dotMesh = new THREE.Mesh(dotGeo, dotMat);
        dotMesh.position.copy(pt);
        scene.add(dotMesh);

        if (measurePoints.length === 2) {
            // Draw Line
            const p1 = measurePoints[0];
            const p2 = measurePoints[1];
            const dist = p1.distanceTo(p2);

            const lineGeo = new THREE.BufferGeometry().setFromPoints([p1, p2]);
            const lineMat = new THREE.LineBasicMaterial({ color: 0xffcc00, linewidth: 3 });
            measureLine = new THREE.Line(lineGeo, lineMat);
            scene.add(measureLine);

            const info = document.getElementById('measure-info');
            if (info) {
                info.innerHTML = `📏 Distância: <b>${dist.toFixed(2)} m</b> (${(dist * 100).toFixed(0)} cm)`;
            }
            measurePoints = [];
        }
    }
}

function clearMeasure() {
    measurePoints = [];
    if (measureLine) {
        scene.remove(measureLine);
        measureLine = null;
    }
    const info = document.getElementById('measure-info');
    if (info) info.innerHTML = '📏 Clique em dois pontos para medir';
}

// Animation Loop
function animate() {
    requestAnimationFrame(animate);

    const dt = clock.getDelta();

    if (currentMode === 'orbit' || currentMode === 'plan') {
        orbitControls.update();
    } else if (currentMode === 'fps') {
        updateFPSMovement(dt);
    }

    renderMinimap();
    renderer.render(scene, camera);
}

// UI Helpers (called from HTML buttons)
window.setMode = setMode;
window.teleportTo = teleportTo;
window.setWallsHeight = setWallsHeight;
window.setupLighting = setupLighting;
window.toggleCeiling = function(checked) {
    ceilingGroup.visible = checked;
};
window.toggleOverlay = function(checked) {
    if (floorPlanMesh) floorPlanMesh.visible = checked;
};
window.toggleLabels = function(checked) {
    labelsGroup.visible = checked;
};
window.toggleMeasure = toggleMeasure;

// Init on DOM ready
window.addEventListener('DOMContentLoaded', init);
