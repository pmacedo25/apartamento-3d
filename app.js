// HI VIEW ALTO DA BOA VISTA - 3D INTERACTIVE ARCHITECTURAL VIEWER
// Proportions extracted 1:1 from Official Blueprint (Scale 1:75, 125.79 m²)
// 100% Compatible with all mobile devices (Firefox Android, Chrome, Safari iOS)
// Anthropometric Calibration: 1.70m Person (Eye Level: 1.60m)
// Daylight Clear Lighting (No Shadows, Bright & Airy)
// Full Meticulous Architectural Model: Walls, Pillars, Shafts, Built-in Fixtures, Interactive Doors

let scene, camera, renderer, orbitControls;
let currentMode = 'orbit'; // 'orbit', 'fps', 'plan'
let apartmentGroup, wallsGroup, floorsGroup, labelsGroup, ceilingGroup, doorsGroup;
let pillarsGroup, shaftsGroup, fixturesGroup;
let floorPlanMesh = null;
let measurePoints = [];
let measureLine = null;
let isMeasuring = false;

// Device check
const isMobile = /Android|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i.test(navigator.userAgent) || (window.innerWidth < 768);

// Anthropometric First Person State (Person: 1.70m -> Eye Level: 1.60m)
const player = {
    pos: null,
    rotY: -Math.PI / 2, // Looking toward terrace
    pitch: 0,
    speed: 1.6, // Realistic human walking speed: ~5.8 km/h
    sprintMultiplier: 1.65,
    radius: 0.28,
    height: 1.60 // Standard eye line for a 1.70m tall person
};
const keys = { w: false, a: false, s: false, d: false, shift: false };
const touchJoystick = { active: false, startX: 0, startY: 0, moveX: 0, moveZ: 0 };
let isPointerLocked = false;
let isDraggingFPS = false;
let prevMousePos = { x: 0, y: 0 };
let currentRoom = null;

// Interactive Doors
const interactiveDoors = [];
let nearestDoor = null;

// Clock
let clock;

// Textures cache
const textures = {};

// Safe Rounded Rect for Canvas 2D
function drawRoundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.quadraticCurveTo(x + w, y, x + w, y + r);
    ctx.lineTo(x + w, y + h - r);
    ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    ctx.lineTo(x + r, y + h);
    ctx.quadraticCurveTo(x, y + h, x, y + h - r);
    ctx.lineTo(x, y + r);
    ctx.quadraticCurveTo(x, y, x + r, y);
    ctx.closePath();
}

// Resilient WebGL Renderer Factory (Guaranteed to work on Firefox Mobile Android & iOS)
function createSafeRenderer(container) {
    const canvas = document.createElement('canvas');
    let glRenderer = null;

    // Strategy 1: Standard WebGLRenderer with lightweight parameters
    try {
        glRenderer = new THREE.WebGLRenderer({
            canvas: canvas,
            antialias: !isMobile && (window.devicePixelRatio || 1) < 2,
            powerPreference: 'default',
            alpha: false,
            depth: true,
            stencil: false,
            failIfMajorPerformanceCaveat: false
        });
    } catch (e1) {
        console.warn('WebGLRenderer standard failed, trying WebGL1 fallback:', e1);
    }

    // Strategy 2: WebGL1Renderer (Three.js fallback for older Gecko/Blink GPUs)
    if (!glRenderer && typeof THREE.WebGL1Renderer === 'function') {
        try {
            glRenderer = new THREE.WebGL1Renderer({
                canvas: canvas,
                antialias: false,
                alpha: false,
                depth: true,
                stencil: false
            });
        } catch (e2) {
            console.warn('WebGL1Renderer failed:', e2);
        }
    }

    // Strategy 3: Explicit WebGL 1 context
    if (!glRenderer) {
        try {
            const gl = canvas.getContext('webgl', { antialias: false, alpha: false }) ||
                       canvas.getContext('experimental-webgl', { antialias: false, alpha: false });
            if (gl) {
                glRenderer = new THREE.WebGLRenderer({
                    canvas: canvas,
                    context: gl,
                    antialias: false,
                    alpha: false
                });
            }
        } catch (e3) {
            console.warn('Explicit context initialization failed:', e3);
        }
    }

    if (!glRenderer) {
        throw new Error('Não foi possível iniciar o WebGL no seu navegador. No Firefox Mobile, certifique-se de que a aceleração gráfica está habilitada.');
    }

    glRenderer.setSize(window.innerWidth, window.innerHeight);
    glRenderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, isMobile ? 1.5 : 2));
    
    // ZERO SHADOW MAPS: Eliminates GPU depth buffer overhead and solves Firefox Mobile black screen/crashes!
    glRenderer.shadowMap.enabled = false;

    if (THREE.ACESFilmicToneMapping) {
        glRenderer.toneMapping = THREE.ACESFilmicToneMapping;
        glRenderer.toneMappingExposure = 1.05;
    }

    container.appendChild(glRenderer.domElement);

    // Context loss handler
    canvas.addEventListener('webglcontextlost', (e) => {
        e.preventDefault();
        console.warn('WebGL Context Lost. Aguardando restauração...');
    }, false);

    canvas.addEventListener('webglcontextrestored', () => {
        console.info('WebGL Context Restored.');
        init();
    }, false);

    return glRenderer;
}

function init() {
    try {
        clock = new THREE.Clock();
        player.pos = new THREE.Vector3(7.20, player.height, 4.50);

        const container = document.getElementById('viewport-container');
        if (!container) throw new Error('Elemento #viewport-container não encontrado');
        container.innerHTML = '';

        // Scene
        scene = new THREE.Scene();
        scene.background = new THREE.Color(0xf0f3f6);
        scene.fog = null;

        // Camera
        camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.08, 150);

        // WebGL Renderer
        renderer = createSafeRenderer(container);

        // Orbit Controls
        if (typeof THREE.OrbitControls === 'function') {
            orbitControls = new THREE.OrbitControls(camera, renderer.domElement);
            orbitControls.enableDamping = true;
            orbitControls.dampingFactor = 0.08;
            orbitControls.maxPolarAngle = Math.PI / 2 - 0.02;
            orbitControls.minDistance = 2;
            orbitControls.maxDistance = 50;
            orbitControls.touches = {
                ONE: THREE.TOUCH.ROTATE,
                TWO: THREE.TOUCH.DOLLY_PAN
            };
        }

        // Groups
        apartmentGroup = new THREE.Group();
        wallsGroup = new THREE.Group();
        floorsGroup = new THREE.Group();
        pillarsGroup = new THREE.Group();
        shaftsGroup = new THREE.Group();
        fixturesGroup = new THREE.Group();
        labelsGroup = new THREE.Group();
        ceilingGroup = new THREE.Group();
        doorsGroup = new THREE.Group();

        apartmentGroup.add(floorsGroup);
        apartmentGroup.add(wallsGroup);
        apartmentGroup.add(pillarsGroup);
        apartmentGroup.add(shaftsGroup);
        apartmentGroup.add(fixturesGroup);
        apartmentGroup.add(doorsGroup);
        apartmentGroup.add(ceilingGroup);
        apartmentGroup.add(labelsGroup);
        scene.add(apartmentGroup);

        // Center apartment in the world
        apartmentGroup.position.set(-6.87, 0, -5.72);

        // Generate Procedural Metric Textures
        initTextures();

        // Setup Bright Clear Lighting (No murky shadows)
        setupLighting('day');

        // Build Architectural Geometry
        buildFloors();
        buildWalls();
        buildPillars();
        buildShafts();
        buildFixtures();
        buildFloorPlanOverlay();
        buildRoomLabels();

        // Setup Initial Camera Mode
        setMode('orbit');

        // Setup Event Listeners & Door Interaction
        setupEvents();

        // Minimap
        initMinimap();

        const errorEl = document.getElementById('webgl-error');
        if (errorEl) errorEl.style.display = 'none';

        // Start Loop
        animate();

    } catch (err) {
        console.error('Erro na inicialização 3D:', err);
        showErrorOnScreen(err.message || err);
    }
}

function showErrorOnScreen(msg) {
    let errDiv = document.getElementById('webgl-error');
    if (!errDiv) {
        errDiv = document.createElement('div');
        errDiv.id = 'webgl-error';
        errDiv.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:#221818;border:2px solid #e04444;color:#fff;padding:24px;border-radius:12px;z-index:9999;font-family:sans-serif;max-width:90%;text-align:center;box-shadow:0 12px 40px rgba(0,0,0,0.8);';
        document.body.appendChild(errDiv);
    }
    errDiv.innerHTML = `
        <h3 style="color:#ff6b6b;margin-bottom:10px;">Erro ao carregar o 3D</h3>
        <p style="font-size:14px;color:#ccc;margin-bottom:14px;">${msg}</p>
        <button onclick="location.reload()" style="background:#c5a882;border:0;color:#121316;padding:8px 18px;border-radius:6px;font-weight:700;cursor:pointer;">Recarregar</button>
    `;
    errDiv.style.display = 'block';
}

function showDoorToast(msg) {
    let toast = document.getElementById('door-toast');
    if (!toast) return;
    toast.innerText = msg;
    toast.style.display = 'block';
    toast.style.opacity = '1';
    clearTimeout(toast._timeout);
    toast._timeout = setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => { toast.style.display = 'none'; }, 300);
    }, 1400);
}

// Procedural Canvas Textures for PBR (High albedo, bright and clean)
function initTextures() {
    try {
        // 1. Porcelain Tile (Living / Kitchen / Hall)
        const cvPorcelain = document.createElement('canvas');
        cvPorcelain.width = 256; cvPorcelain.height = 256;
        const ctxP = cvPorcelain.getContext('2d');
        ctxP.fillStyle = '#f7f5ef';
        ctxP.fillRect(0, 0, 256, 256);
        ctxP.strokeStyle = '#e3ded3';
        ctxP.lineWidth = 3;
        ctxP.strokeRect(1, 1, 254, 254);
        const texPorcelain = new THREE.CanvasTexture(cvPorcelain);
        texPorcelain.wrapS = THREE.RepeatWrapping;
        texPorcelain.wrapT = THREE.RepeatWrapping;
        textures.porcelain = texPorcelain;

        // 2. Wood Laminate Planks (Suites & Circulation)
        const cvWood = document.createElement('canvas');
        cvWood.width = 256; cvWood.height = 256;
        const ctxW = cvWood.getContext('2d');
        ctxW.fillStyle = '#ceb494';
        ctxW.fillRect(0, 0, 256, 256);
        for (let y = 0; y < 256; y += 42) {
            ctxW.strokeStyle = '#ab8e6a';
            ctxW.lineWidth = 2;
            ctxW.beginPath(); ctxW.moveTo(0, y); ctxW.lineTo(256, y); ctxW.stroke();
        }
        const texWood = new THREE.CanvasTexture(cvWood);
        texWood.wrapS = THREE.RepeatWrapping;
        texWood.wrapT = THREE.RepeatWrapping;
        textures.wood = texWood;

        // 3. Terrace Outdoor Tile (Gourmet)
        const cvTerrace = document.createElement('canvas');
        cvTerrace.width = 256; cvTerrace.height = 256;
        const ctxT = cvTerrace.getContext('2d');
        ctxT.fillStyle = '#c7c0b3';
        ctxT.fillRect(0, 0, 256, 256);
        ctxT.strokeStyle = '#a69f91';
        ctxT.lineWidth = 3;
        ctxT.strokeRect(1, 1, 254, 254);
        const texTerrace = new THREE.CanvasTexture(cvTerrace);
        texTerrace.wrapS = THREE.RepeatWrapping;
        texTerrace.wrapT = THREE.RepeatWrapping;
        textures.terrace = texTerrace;

        // 4. Bath Tile / Ceramic
        const cvBath = document.createElement('canvas');
        cvBath.width = 256; cvBath.height = 256;
        const ctxB = cvBath.getContext('2d');
        ctxB.fillStyle = '#f2efe9';
        ctxB.fillRect(0, 0, 256, 256);
        ctxB.strokeStyle = '#d4cfc5';
        ctxB.lineWidth = 3;
        ctxB.strokeRect(1, 1, 254, 254);
        const texBath = new THREE.CanvasTexture(cvBath);
        texBath.wrapS = THREE.RepeatWrapping;
        texBath.wrapT = THREE.RepeatWrapping;
        textures.bath = texBath;
    } catch(e) {
        console.warn('Erro ao criar texturas procedurais:', e);
    }
}

// Lighting Setup: 100% Shadowless, Bright, Crisp & Architectural
let dirLight, fillLight, hemiLight, ambientLight, ceilingLights = [];
function setupLighting(preset = 'day') {
    if (dirLight) scene.remove(dirLight);
    if (fillLight) scene.remove(fillLight);
    if (hemiLight) scene.remove(hemiLight);
    if (ambientLight) scene.remove(ambientLight);
    ceilingLights.forEach(l => scene.remove(l));
    ceilingLights = [];

    if (preset === 'day') {
        scene.background = new THREE.Color(0xf0f3f6);

        hemiLight = new THREE.HemisphereLight(0xffffff, 0xdfe5ed, 0.95);
        scene.add(hemiLight);

        dirLight = new THREE.DirectionalLight(0xfffbf2, 0.85);
        dirLight.position.set(-12, 18, 6);
        scene.add(dirLight);

        fillLight = new THREE.DirectionalLight(0xe8f0fc, 0.45);
        fillLight.position.set(12, 14, -8);
        scene.add(fillLight);

        ambientLight = new THREE.AmbientLight(0xffffff, 0.35);
        scene.add(ambientLight);

    } else if (preset === 'sunset') {
        scene.background = new THREE.Color(0x232026);

        hemiLight = new THREE.HemisphereLight(0xffe2cc, 0x4a434d, 0.85);
        scene.add(hemiLight);

        dirLight = new THREE.DirectionalLight(0xffa055, 1.1);
        dirLight.position.set(-16, 8, 8);
        scene.add(dirLight);

        ambientLight = new THREE.AmbientLight(0xfff0e6, 0.35);
        scene.add(ambientLight);

    } else if (preset === 'night') {
        scene.background = new THREE.Color(0x121418);

        hemiLight = new THREE.HemisphereLight(0x353b47, 0x14161c, 0.45);
        scene.add(hemiLight);

        ambientLight = new THREE.AmbientLight(0x444b59, 0.3);
        scene.add(ambientLight);

        APARTMENT_DATA.rooms.forEach(room => {
            const cx = (room.box[0] + room.box[2]) / 2 - 6.87;
            const cz = (room.box[1] + room.box[3]) / 2 - 5.72;
            const light = new THREE.PointLight(0xffeed6, 0.95, 7.5);
            light.position.set(cx, 2.55, cz);
            scene.add(light);
            ceilingLights.push(light);

            const spotGeo = new THREE.SphereGeometry(0.06, 8, 8);
            const spotMat = new THREE.MeshBasicMaterial({ color: 0xffeedd });
            const spotMesh = new THREE.Mesh(spotGeo, spotMat);
            spotMesh.position.copy(light.position);
            scene.add(spotMesh);
            ceilingLights.push(spotMesh);
        });
    }
}

// Build Floors with Exact Real-World Metric Tile Scale
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

        let floorBaseTex = textures.porcelain;
        let tileW = 0.90; // 90cm porcelain slabs
        let tileD = 0.90;
        let roughness = 0.35;
        let metalness = 0.05;

        if (room.floor === 'wood') {
            floorBaseTex = textures.wood;
            tileW = 1.20; // 1.20m wood planks
            tileD = 0.20;
            roughness = 0.55;
        } else if (room.floor === 'deck_or_tile') {
            floorBaseTex = textures.terrace;
            tileW = 0.60;
            tileD = 0.60;
            roughness = 0.6;
        } else if (room.floor === 'tile_light' || room.floor === 'tile_dark' || room.floor === 'concrete') {
            floorBaseTex = textures.bath;
            tileW = 0.60;
            tileD = 0.60;
            roughness = 0.35;
        }

        let roomTex = null;
        if (floorBaseTex) {
            roomTex = floorBaseTex.clone();
            roomTex.needsUpdate = true;
            roomTex.repeat.set(w / tileW, d / tileD);
        }

        const floorMat = new THREE.MeshStandardMaterial({
            map: roomTex || null,
            color: roomTex ? 0xffffff : 0xdddddd,
            roughness: roughness,
            metalness: metalness
        });

        const floorGeo = new THREE.PlaneGeometry(w, d);
        const floorMesh = new THREE.Mesh(floorGeo, floorMat);
        floorMesh.rotation.x = -Math.PI / 2;
        floorMesh.position.set(cx, 0.001, cz);
        floorMesh.userData = { room: room };
        floorsGroup.add(floorMesh);

        // Ceiling (removable)
        const ceilGeo = new THREE.PlaneGeometry(w, d);
        const ceilMat = new THREE.MeshStandardMaterial({
            color: 0xffffff,
            roughness: 0.85,
            side: THREE.DoubleSide
        });
        const ceilMesh = new THREE.Mesh(ceilGeo, ceilMat);
        ceilMesh.rotation.x = Math.PI / 2;
        ceilMesh.position.set(cx, 2.70, cz);
        ceilingGroup.add(ceilMesh);
    });

    // Base ground slab underneath apartment
    const slabGeo = new THREE.BoxGeometry(15, 0.2, 13);
    const slabMat = new THREE.MeshStandardMaterial({ color: 0xe2e6eb, roughness: 0.9 });
    const slabMesh = new THREE.Mesh(slabGeo, slabMat);
    slabMesh.position.set(6.87, -0.1, 5.72);
    floorsGroup.add(slabMesh);
}

// Materials
const wallMaterial = new THREE.MeshStandardMaterial({ color: 0xfcfbfa, roughness: 0.75, metalness: 0.0 });
const baseboardMaterial = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.35 });
const pillarMaterial = new THREE.MeshStandardMaterial({ color: 0xe6e4df, roughness: 0.80, metalness: 0.05 });
const shaftMaterial = new THREE.MeshStandardMaterial({ color: 0xf8f6f0, roughness: 0.75, metalness: 0.0 });
const beamMaterial = new THREE.MeshStandardMaterial({ color: 0xf4f2ee, roughness: 0.80, metalness: 0.0 });
const graniteBlackMat = new THREE.MeshStandardMaterial({ color: 0x242528, roughness: 0.25, metalness: 0.1 });
const marbleLightMat = new THREE.MeshStandardMaterial({ color: 0xf2eee7, roughness: 0.20, metalness: 0.05 });
const ceramicWhiteMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.15, metalness: 0.05 });
const chromeMat = new THREE.MeshStandardMaterial({ color: 0xdddddd, roughness: 0.15, metalness: 0.95 });
const steelSinkMat = new THREE.MeshStandardMaterial({ color: 0xcccccc, roughness: 0.25, metalness: 0.85 });
const glassMaterial = new THREE.MeshStandardMaterial({ color: 0x9ec7db, transparent: true, opacity: 0.35, roughness: 0.1, metalness: 0.1, side: THREE.DoubleSide, depthWrite: false });
const showerGlassMat = new THREE.MeshStandardMaterial({ color: 0xa8d4e6, transparent: true, opacity: 0.45, roughness: 0.1, metalness: 0.1, side: THREE.DoubleSide, depthWrite: false });
const frameMaterial = new THREE.MeshStandardMaterial({ color: 0x222428, roughness: 0.4, metalness: 0.5 });
const doorWoodMaterial = new THREE.MeshStandardMaterial({ color: 0xd6c2a8, roughness: 0.45, metalness: 0.05 });

function buildWalls() {
    interactiveDoors.length = 0;

    APARTMENT_DATA.walls.forEach(w => {
        const dx = w.x2 - w.x1;
        const dz = w.z2 - w.z1;
        const len = Math.hypot(dx, dz);
        if (len < 0.05) return;

        const angle = Math.atan2(dz, dx);
        const wallHeight = w.height || 2.70;
        const thick = w.thick || 0.15;

        const wallObj = new THREE.Group();
        wallObj.position.set(w.x1, 0, w.z1);
        wallObj.rotation.y = -angle;
        wallObj.userData = { wallData: w, baseHeight: wallHeight };

        if (w.type === 'railing') {
            buildBalconyRailing(wallObj, len, 1.20, thick);
            wallsGroup.add(wallObj);
            return;
        }

        if (w.type === 'beam') {
            // Overhead dropped structural beam
            const beamGeo = new THREE.BoxGeometry(len, wallHeight, thick);
            const beamMesh = new THREE.Mesh(beamGeo, beamMaterial);
            beamMesh.position.set(len / 2, 2.70 - wallHeight / 2, 0);
            wallObj.add(beamMesh);
            wallsGroup.add(wallObj);
            return;
        }

        if (w.type === 'countertop') {
            const topGeo = new THREE.BoxGeometry(len, 0.95, thick);
            const topMesh = new THREE.Mesh(topGeo, graniteBlackMat);
            topMesh.position.set(len / 2, 0.475, 0);
            wallObj.add(topMesh);
            wallsGroup.add(wallObj);
            return;
        }

        if (w.type === 'sliding_glass_wall') {
            buildSlidingGlassWall(wallObj, len, wallHeight, thick);
            wallsGroup.add(wallObj);
            return;
        }

        // Standard wall with doors/windows
        if (!w.openings || w.openings.length === 0) {
            const solidGeo = new THREE.BoxGeometry(len, wallHeight, thick);
            const solidMesh = new THREE.Mesh(solidGeo, wallMaterial);
            solidMesh.position.set(len / 2, wallHeight / 2, 0);
            wallObj.add(solidMesh);

            const bbGeo = new THREE.BoxGeometry(len, 0.14, thick + 0.02);
            const bbMesh = new THREE.Mesh(bbGeo, baseboardMaterial);
            bbMesh.position.set(len / 2, 0.07, 0);
            wallObj.add(bbMesh);
        } else {
            let currentX = 0;
            w.openings.sort((a, b) => a.start - b.start);

            w.openings.forEach((op) => {
                const opStart = Math.max(0, op.start);
                const opEnd = Math.min(len, opStart + op.width);
                const segLen = opStart - currentX;

                if (segLen > 0.02) {
                    const segGeo = new THREE.BoxGeometry(segLen, wallHeight, thick);
                    const segMesh = new THREE.Mesh(segGeo, wallMaterial);
                    segMesh.position.set(currentX + segLen / 2, wallHeight / 2, 0);
                    wallObj.add(segMesh);

                    const bbGeo = new THREE.BoxGeometry(segLen, 0.14, thick + 0.02);
                    const bbMesh = new THREE.Mesh(bbGeo, baseboardMaterial);
                    bbMesh.position.set(currentX + segLen / 2, 0.07, 0);
                    wallObj.add(bbMesh);
                }

                const opW = opEnd - opStart;

                if (op.type === 'door' || op.type === 'opening') {
                    const dh = op.height || 2.10;
                    const lintelH = wallHeight - dh;
                    if (lintelH > 0.02) {
                        const lintelGeo = new THREE.BoxGeometry(opW, lintelH, thick);
                        const lintelMesh = new THREE.Mesh(lintelGeo, wallMaterial);
                        lintelMesh.position.set(opStart + opW / 2, dh + lintelH / 2, 0);
                        wallObj.add(lintelMesh);
                    }

                    if (op.type === 'door') {
                        buildDoorFrameAndLeaf(wallObj, opStart, opW, dh, thick, op);
                    }
                } else if (op.type === 'window' || op.type === 'ventilation') {
                    const sill = op.sill || 0.90;
                    const wh = op.height || 1.30;
                    if (sill > 0.02) {
                        const sillGeo = new THREE.BoxGeometry(opW, sill, thick);
                        const sillMesh = new THREE.Mesh(sillGeo, wallMaterial);
                        sillMesh.position.set(opStart + opW / 2, sill / 2, 0);
                        wallObj.add(sillMesh);

                        const bbGeo = new THREE.BoxGeometry(opW, 0.14, thick + 0.02);
                        const bbMesh = new THREE.Mesh(bbGeo, baseboardMaterial);
                        bbMesh.position.set(opStart + opW / 2, 0.07, 0);
                        wallObj.add(bbMesh);
                    }

                    const topY = sill + wh;
                    const lintelH = wallHeight - topY;
                    if (lintelH > 0.02) {
                        const lintelGeo = new THREE.BoxGeometry(opW, lintelH, thick);
                        const lintelMesh = new THREE.Mesh(lintelGeo, wallMaterial);
                        lintelMesh.position.set(opStart + opW / 2, topY + lintelH / 2, 0);
                        wallObj.add(lintelMesh);
                    }

                    buildWindowFrameAndGlass(wallObj, opStart, opW, sill, wh, thick);
                }

                currentX = opEnd;
            });

            const remLen = len - currentX;
            if (remLen > 0.02) {
                const segGeo = new THREE.BoxGeometry(remLen, wallHeight, thick);
                const segMesh = new THREE.Mesh(segGeo, wallMaterial);
                segMesh.position.set(currentX + remLen / 2, wallHeight / 2, 0);
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

// Build Structural Concrete Pillars (Pilares Estruturais)
function buildPillars() {
    if (!APARTMENT_DATA.pillars) return;
    APARTMENT_DATA.pillars.forEach(p => {
        const pObj = new THREE.Group();
        pObj.position.set(p.x, 0, p.z);
        pObj.userData = { pillarData: p, baseHeight: p.h || 2.70 };

        const geo = new THREE.BoxGeometry(p.w, p.h || 2.70, p.d);
        const mesh = new THREE.Mesh(geo, pillarMaterial);
        mesh.position.set(p.w / 2, (p.h || 2.70) / 2, p.d / 2);
        pObj.add(mesh);

        // Skirting / Baseboard around pillar
        const bbGeo = new THREE.BoxGeometry(p.w + 0.02, 0.14, p.d + 0.02);
        const bbMesh = new THREE.Mesh(bbGeo, baseboardMaterial);
        bbMesh.position.set(p.w / 2, 0.07, p.d / 2);
        pObj.add(bbMesh);

        pillarsGroup.add(pObj);
    });
}

// Build Technical Shafts (Shafts Hidráulicos / Ventilação)
function buildShafts() {
    if (!APARTMENT_DATA.shafts) return;
    APARTMENT_DATA.shafts.forEach(s => {
        const sObj = new THREE.Group();
        sObj.position.set(s.x, 0, s.z);
        sObj.userData = { shaftData: s, baseHeight: s.h || 2.70 };

        const geo = new THREE.BoxGeometry(s.w, s.h || 2.70, s.d);
        const mesh = new THREE.Mesh(geo, shaftMaterial);
        mesh.position.set(s.w / 2, (s.h || 2.70) / 2, s.d / 2);
        sObj.add(mesh);

        // Baseboard
        const bbGeo = new THREE.BoxGeometry(s.w + 0.02, 0.14, s.d + 0.02);
        const bbMesh = new THREE.Mesh(bbGeo, baseboardMaterial);
        bbMesh.position.set(s.w / 2, 0.07, s.d / 2);
        sObj.add(bbMesh);

        shaftsGroup.add(sObj);
    });
}

// Build Built-in Fixed Architectural Fixtures (Bancadas, pias, churrasqueira, louças, boxes)
function buildFixtures() {
    if (!APARTMENT_DATA.fixtures) return;

    APARTMENT_DATA.fixtures.forEach(f => {
        const grp = new THREE.Group();
        grp.position.set(f.x, 0, f.z);

        if (f.type === 'counter_sink') {
            // Kitchen Countertop
            const topGeo = new THREE.BoxGeometry(f.w, f.h, f.d);
            const topMesh = new THREE.Mesh(topGeo, graniteBlackMat);
            topMesh.position.set(f.w / 2, f.h / 2, f.d / 2);
            grp.add(topMesh);

            // Stainless Steel Sink
            const sinkX = f.sink_x ? f.sink_x - f.x : f.w / 2;
            const sinkGeo = new THREE.BoxGeometry(0.60, 0.02, 0.40);
            const sinkMesh = new THREE.Mesh(sinkGeo, steelSinkMat);
            sinkMesh.position.set(sinkX, f.h + 0.005, f.d / 2);
            grp.add(sinkMesh);

            // Chrome Faucet
            buildFaucet(grp, sinkX, f.h + 0.01, f.d / 2 - 0.14);

        } else if (f.type === 'laundry_tub') {
            // Service laundry sink
            const tubGeo = new THREE.BoxGeometry(f.w, f.h, f.d);
            const tubMesh = new THREE.Mesh(tubGeo, ceramicWhiteMat);
            tubMesh.position.set(f.w / 2, f.h / 2, f.d / 2);
            grp.add(tubMesh);

            // Inset bowl
            const bowlGeo = new THREE.BoxGeometry(f.w - 0.14, 0.28, f.d - 0.14);
            const bowlMat = new THREE.MeshStandardMaterial({ color: 0xefefef, roughness: 0.15 });
            const bowlMesh = new THREE.Mesh(bowlGeo, bowlMat);
            bowlMesh.position.set(f.w / 2, f.h - 0.14, f.d / 2);
            grp.add(bowlMesh);

            buildFaucet(grp, f.w / 2, f.h + 0.01, 0.08);

        } else if (f.type === 'gourmet_counter') {
            // Barbecue Countertop
            const topGeo = new THREE.BoxGeometry(f.w, f.h, f.d);
            const topMesh = new THREE.Mesh(topGeo, graniteBlackMat);
            topMesh.position.set(f.w / 2, f.h / 2, f.d / 2);
            grp.add(topMesh);

            // Round sink
            const sinkGeo = new THREE.CylinderGeometry(0.18, 0.18, 0.02, 24);
            const sinkMesh = new THREE.Mesh(sinkGeo, steelSinkMat);
            sinkMesh.position.set(0.35, f.h + 0.005, f.d / 2);
            grp.add(sinkMesh);
            buildFaucet(grp, 0.35, f.h + 0.01, f.d / 2 - 0.14);

            // Barbecue grill niche
            const bbqGeo = new THREE.BoxGeometry(f.bbq_w || 0.45, 0.04, f.d - 0.12);
            const bbqMat = new THREE.MeshStandardMaterial({ color: 0x111111, roughness: 0.8 });
            const bbqMesh = new THREE.Mesh(bbqGeo, bbqMat);
            bbqMesh.position.set(f.w - (f.bbq_w || 0.45) / 2 - 0.08, f.h + 0.01, f.d / 2);
            grp.add(bbqMesh);

        } else if (f.type === 'double_vanity') {
            // Master Double Vanity
            const topGeo = new THREE.BoxGeometry(f.w, f.h, f.d);
            const topMesh = new THREE.Mesh(topGeo, marbleLightMat);
            topMesh.position.set(f.w / 2, f.h / 2, f.d / 2);
            grp.add(topMesh);

            // Sink 1 & 2
            const z1 = f.sink_z1 - f.z;
            const z2 = f.sink_z2 - f.z;

            [z1, z2].forEach(zPos => {
                const sGeo = new THREE.BoxGeometry(f.w - 0.16, 0.02, 0.38);
                const sMesh = new THREE.Mesh(sGeo, ceramicWhiteMat);
                sMesh.position.set(f.w / 2, f.h + 0.005, zPos);
                grp.add(sMesh);

                buildFaucet(grp, 0.08, f.h + 0.01, zPos, 'side');
            });

        } else if (f.type === 'vanity') {
            // Single Bathroom Vanity
            const topGeo = new THREE.BoxGeometry(f.w, f.h, f.d);
            const topMesh = new THREE.Mesh(topGeo, marbleLightMat);
            topMesh.position.set(f.w / 2, f.h / 2, f.d / 2);
            grp.add(topMesh);

            const sGeo = new THREE.BoxGeometry(Math.min(0.42, f.w - 0.14), 0.02, Math.min(0.38, f.d - 0.14));
            const sMesh = new THREE.Mesh(sGeo, ceramicWhiteMat);
            sMesh.position.set(f.w / 2, f.h + 0.005, f.d / 2);
            grp.add(sMesh);

            buildFaucet(grp, f.w / 2, f.h + 0.01, 0.08);

        } else if (f.type === 'toilet') {
            // Toilet with Flush Tank
            const bowlGeo = new THREE.BoxGeometry(f.w, 0.42, f.d - 0.20);
            const bowlMesh = new THREE.Mesh(bowlGeo, ceramicWhiteMat);
            bowlMesh.position.set(f.w / 2, 0.21, f.d / 2 + 0.05);
            grp.add(bowlMesh);

            const tankGeo = new THREE.BoxGeometry(f.w, 0.38, 0.18);
            const tankMesh = new THREE.Mesh(tankGeo, ceramicWhiteMat);
            tankMesh.position.set(f.w / 2, 0.58, 0.09);
            grp.add(tankMesh);

            const btnGeo = new THREE.CylinderGeometry(0.025, 0.025, 0.015, 16);
            const btnMesh = new THREE.Mesh(btnGeo, chromeMat);
            btnMesh.position.set(f.w / 2, 0.775, 0.09);
            grp.add(btnMesh);

            if (f.rotY) grp.rotation.y = f.rotY;

        } else if (f.type === 'shower_box') {
            // Glass Shower Screen
            const isHorizontal = f.w > f.d;
            const glassLen = isHorizontal ? f.w : f.d;
            const glassGeo = new THREE.BoxGeometry(isHorizontal ? glassLen : 0.015, f.h, isHorizontal ? 0.015 : glassLen);
            const glassMesh = new THREE.Mesh(glassGeo, showerGlassMat);
            glassMesh.position.set(f.w / 2, f.h / 2, f.d / 2);
            grp.add(glassMesh);

            // Shower Head
            if (f.shower_pos) {
                const sGrp = new THREE.Group();
                sGrp.position.set(f.shower_pos[0] - f.x, f.shower_pos[1], f.shower_pos[2] - f.z);

                const armGeo = new THREE.CylinderGeometry(0.015, 0.015, 0.35, 8);
                const armMesh = new THREE.Mesh(armGeo, chromeMat);
                armMesh.rotation.x = Math.PI / 2;
                sGrp.add(armMesh);

                const headGeo = new THREE.CylinderGeometry(0.12, 0.12, 0.02, 24);
                const headMesh = new THREE.Mesh(headGeo, chromeMat);
                headMesh.position.set(0, -0.06, 0.18);
                sGrp.add(headMesh);

                grp.add(sGrp);
            }
        }

        fixturesGroup.add(grp);
    });
}

function buildFaucet(parentGroup, x, y, z, orient = 'front') {
    const fGrp = new THREE.Group();
    fGrp.position.set(x, y, z);

    const baseGeo = new THREE.CylinderGeometry(0.025, 0.025, 0.04, 12);
    const baseMesh = new THREE.Mesh(baseGeo, chromeMat);
    baseMesh.position.y = 0.02;
    fGrp.add(baseMesh);

    const spoutGeo = new THREE.TorusGeometry(0.08, 0.015, 8, 16, Math.PI / 1.2);
    const spoutMesh = new THREE.Mesh(spoutGeo, chromeMat);
    spoutMesh.position.set(0, 0.10, orient === 'side' ? 0.04 : 0.04);
    if (orient === 'side') spoutMesh.rotation.y = Math.PI / 2;
    fGrp.add(spoutMesh);

    parentGroup.add(fGrp);
}

function buildBalconyRailing(group, len, h, thick) {
    const glassGeo = new THREE.BoxGeometry(len, h - 0.10, 0.02);
    const glassMesh = new THREE.Mesh(glassGeo, glassMaterial);
    glassMesh.position.set(len / 2, h / 2, 0);
    group.add(glassMesh);

    const railGeo = new THREE.BoxGeometry(len, 0.06, 0.08);
    const railMesh = new THREE.Mesh(railGeo, frameMaterial);
    railMesh.position.set(len / 2, h - 0.03, 0);
    group.add(railMesh);

    const baseGeo = new THREE.BoxGeometry(len, 0.08, thick);
    const baseMesh = new THREE.Mesh(baseGeo, wallMaterial);
    baseMesh.position.set(len / 2, 0.04, 0);
    group.add(baseMesh);

    const numPosts = Math.max(2, Math.round(len / 1.2));
    for (let i = 0; i <= numPosts; i++) {
        const px = (len / numPosts) * i;
        const postGeo = new THREE.BoxGeometry(0.04, h, 0.04);
        const postMesh = new THREE.Mesh(postGeo, frameMaterial);
        postMesh.position.set(px, h / 2, 0);
        group.add(postMesh);
    }
}

function buildSlidingGlassWall(group, len, h, thick) {
    const doorH = 2.45;
    const lintelH = h - doorH;

    if (lintelH > 0.02) {
        const topGeo = new THREE.BoxGeometry(len, lintelH, thick);
        const topMesh = new THREE.Mesh(topGeo, wallMaterial);
        topMesh.position.set(len / 2, doorH + lintelH / 2, 0);
        group.add(topMesh);
    }

    const panelW = len / 4;
    for (let i = 0; i < 4; i++) {
        const px = panelW * i + panelW / 2;
        const pz = (i % 2 === 0 ? 0.03 : -0.03);

        const fGeo = new THREE.BoxGeometry(panelW - 0.04, doorH, 0.04);
        const gGeo = new THREE.BoxGeometry(panelW - 0.12, doorH - 0.12, 0.015);
        const gMesh = new THREE.Mesh(gGeo, glassMaterial);
        gMesh.position.set(px, doorH / 2, pz);
        group.add(gMesh);

        const frameMesh = new THREE.Mesh(fGeo, frameMaterial);
        frameMesh.position.set(px, doorH / 2, pz);
        group.add(frameMesh);
    }
}

// Interactive Door Frame & Leaf (Starts Closed, Opens on Click/Proximity)
function buildDoorFrameAndLeaf(group, start, w, h, thick, op) {
    const frameThick = 0.04;
    const leftPostGeo = new THREE.BoxGeometry(frameThick, h, thick + 0.01);
    const leftPost = new THREE.Mesh(leftPostGeo, frameMaterial);
    leftPost.position.set(start + frameThick / 2, h / 2, 0);
    group.add(leftPost);

    const rightPostGeo = new THREE.BoxGeometry(frameThick, h, thick + 0.01);
    const rightPost = new THREE.Mesh(rightPostGeo, frameMaterial);
    rightPost.position.set(start + w - frameThick / 2, h / 2, 0);
    group.add(rightPost);

    const headGeo = new THREE.BoxGeometry(w, frameThick, thick + 0.01);
    const head = new THREE.Mesh(headGeo, frameMaterial);
    head.position.set(start + w / 2, h - frameThick / 2, 0);
    group.add(head);

    const leafW = w - frameThick * 2;
    const leafGeo = new THREE.BoxGeometry(leafW, h - frameThick, 0.04);
    const leafMesh = new THREE.Mesh(leafGeo, doorWoodMaterial);
    leafMesh.position.set(leafW / 2, (h - frameThick) / 2, 0);

    const pivot = new THREE.Group();
    pivot.position.set(start + frameThick, 0, 0);
    pivot.rotation.y = 0; // Starts CLOSED by default!
    pivot.add(leafMesh);

    const handleGeo = new THREE.BoxGeometry(0.12, 0.03, 0.06);
    const handleMesh = new THREE.Mesh(handleGeo, chromeMat);
    handleMesh.position.set(leafW - 0.08, 0.98, 0.03);
    pivot.add(handleMesh);

    group.add(pivot);

    // Invisible Hitbox for comfortable tap/click interaction
    const hitGeo = new THREE.BoxGeometry(w + 0.25, h, thick + 0.5);
    const hitMat = new THREE.MeshBasicMaterial({ visible: false });
    const hitMesh = new THREE.Mesh(hitGeo, hitMat);
    hitMesh.position.set(start + w / 2, h / 2, 0);
    group.add(hitMesh);

    const doorData = {
        id: (op && op.label) || `porta_${interactiveDoors.length}`,
        label: (op && op.label) || 'Porta',
        pivot: pivot,
        group: group,
        leafMesh: leafMesh,
        handleMesh: handleMesh,
        hitMesh: hitMesh,
        isOpen: false,
        currentAngle: 0.0,
        targetAngle: 0.0,
        openAngle: Math.PI * 0.48, // ~86 degrees swing
        worldPos: new THREE.Vector3()
    };

    leafMesh.userData.door = doorData;
    handleMesh.userData.door = doorData;
    hitMesh.userData.door = doorData;

    interactiveDoors.push(doorData);
    doorsGroup.add(pivot);
}

function buildWindowFrameAndGlass(group, start, w, sill, h, thick) {
    const cy = sill + h / 2;
    const cx = start + w / 2;

    const glassGeo = new THREE.BoxGeometry(w - 0.08, h - 0.08, 0.015);
    const glassMesh = new THREE.Mesh(glassGeo, glassMaterial);
    glassMesh.position.set(cx, cy, 0);
    group.add(glassMesh);

    const frameGeo = new THREE.BoxGeometry(w, h, thick * 0.7);
    const frameMesh = new THREE.Mesh(frameGeo, frameMaterial);
    frameMesh.position.set(cx, cy, 0);
    group.add(frameMesh);
}

// Overlay Original Floor Plan on Ground
function buildFloorPlanOverlay() {
    if (typeof PLAN_BASE64 === 'undefined' || !PLAN_BASE64) return;
    try {
        const img = new Image();
        img.src = PLAN_BASE64;
        img.onload = () => {
            const tex = new THREE.Texture(img);
            tex.generateMipmaps = false;
            tex.wrapS = THREE.ClampToEdgeWrapping;
            tex.wrapT = THREE.ClampToEdgeWrapping;
            tex.minFilter = THREE.LinearFilter;
            tex.needsUpdate = true;

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
            floorPlanMesh.visible = false;
            apartmentGroup.add(floorPlanMesh);
        };
    } catch(e) {
        console.warn('Erro ao carregar overlay da planta:', e);
    }
}

// 3D Room Badges (Only displayed in Orbit & 2D Plan; HIDDEN in First Person!)
function buildRoomLabels() {
    try {
        APARTMENT_DATA.rooms.forEach(r => {
            const cx = (r.box[0] + r.box[2]) / 2;
            const cz = (r.box[1] + r.box[3]) / 2;

            const canvas = document.createElement('canvas');
            canvas.width = 256; canvas.height = 128;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = 'rgba(24, 26, 30, 0.82)';
            drawRoundRect(ctx, 4, 4, 248, 120, 16);
            ctx.fill();

            ctx.strokeStyle = '#c5a882';
            ctx.lineWidth = 3;
            ctx.stroke();

            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 22px sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText(r.name, 128, 52);

            ctx.fillStyle = '#c5a882';
            ctx.font = 'bold 20px monospace';
            ctx.fillText(`${r.area.toFixed(1)} m²`, 128, 92);

            const tex = new THREE.CanvasTexture(canvas);
            tex.generateMipmaps = false;
            tex.minFilter = THREE.LinearFilter;
            const spriteMat = new THREE.SpriteMaterial({ map: tex, transparent: true });
            const sprite = new THREE.Sprite(spriteMat);
            sprite.position.set(cx, 1.95, cz);
            sprite.scale.set(1.4, 0.7, 1);
            labelsGroup.add(sprite);
        });
    } catch(e) {
        console.warn('Erro ao criar rótulos 3D:', e);
    }
}

// Toggle Door Open/Close
function toggleDoor(door) {
    if (!door) return;
    door.isOpen = !door.isOpen;
    door.targetAngle = door.isOpen ? door.openAngle : 0.0;
    showDoorToast(`${door.isOpen ? 'Abrindo' : 'Fechando'} ${door.label}...`);
    updateNearestDoorHUD();
}

function triggerNearestDoor() {
    if (nearestDoor) {
        toggleDoor(nearestDoor);
    }
}

// Check Raycast Click on Door
function checkDoorClick(clientX, clientY) {
    const mouse = new THREE.Vector2(
        (clientX / window.innerWidth) * 2 - 1,
        -(clientY / window.innerHeight) * 2 + 1
    );
    const raycaster = new THREE.Raycaster();
    raycaster.setFromCamera(mouse, camera);

    const hitTargets = [];
    interactiveDoors.forEach(d => {
        if (d.hitMesh) hitTargets.push(d.hitMesh);
        if (d.leafMesh) hitTargets.push(d.leafMesh);
        if (d.handleMesh) hitTargets.push(d.handleMesh);
    });

    const intersects = raycaster.intersectObjects(hitTargets, true);
    if (intersects.length > 0) {
        let obj = intersects[0].object;
        while (obj && (!obj.userData || !obj.userData.door)) {
            obj = obj.parent;
        }
        if (obj && obj.userData && obj.userData.door) {
            toggleDoor(obj.userData.door);
            return true;
        }
    }
    return false;
}

// Updates Door HUD in First Person Mode (Proximity Detection)
const tempDoorPos = new THREE.Vector3();
function updateNearestDoorHUD() {
    if (currentMode !== 'fps') {
        const hud = document.getElementById('door-hud');
        if (hud) hud.style.display = 'none';
        const mobBtn = document.getElementById('door-mobile-btn');
        if (mobBtn) mobBtn.style.display = 'none';
        nearestDoor = null;
        return;
    }

    let closest = null;
    let minDist = 2.2;
    const camPos = camera.position;

    interactiveDoors.forEach(d => {
        d.pivot.getWorldPosition(tempDoorPos);
        const dist = camPos.distanceTo(tempDoorPos);
        if (dist < minDist) {
            minDist = dist;
            closest = d;
        }
    });

    nearestDoor = closest;

    const hud = document.getElementById('door-hud');
    const hudText = document.getElementById('door-hud-text');
    const mobBtn = document.getElementById('door-mobile-btn');

    if (closest) {
        const actionLabel = closest.isOpen ? 'Fechar' : 'Abrir';
        if (hud && !isMobile) {
            hudText.innerHTML = `[E] ou Clique para <b>${actionLabel} ${closest.label}</b>`;
            hud.style.display = 'flex';
        }
        if (mobBtn && isMobile) {
            mobBtn.innerHTML = `🚪 ${actionLabel} ${closest.label}`;
            mobBtn.style.display = 'flex';
        }
    } else {
        if (hud) hud.style.display = 'none';
        if (mobBtn) mobBtn.style.display = 'none';
    }
}

// Adjust Observer Eye Height (Custom anthropometric testing)
function setObserverHeight(heightVal) {
    const h = parseFloat(heightVal);
    player.height = h;
    player.pos.y = h;
    if (currentMode === 'fps') {
        camera.position.y = h;
    }
    const label = document.getElementById('observer-height-label');
    if (label) label.innerText = `${h.toFixed(2)} m`;
    const badge = document.getElementById('eye-height-display');
    if (badge) badge.innerText = `${h.toFixed(2)} m`;
}

// Dynamic FOV: Ensures Natural Human Horizontal Field of View (85 deg) even on Portrait Mobile!
function updateCameraFov() {
    const aspect = window.innerWidth / window.innerHeight;
    if (currentMode === 'fps') {
        const desiredHFovRad = 85 * (Math.PI / 180);
        if (aspect < 1.0) {
            const vFovRad = 2 * Math.atan(Math.tan(desiredHFovRad / 2) / aspect);
            camera.fov = Math.min(115, THREE.MathUtils.radToDeg(vFovRad));
        } else {
            camera.fov = 60;
        }
    } else if (currentMode === 'orbit') {
        camera.fov = 48;
    } else if (currentMode === 'plan') {
        camera.fov = 40;
    }
    camera.updateProjectionMatrix();
}

// Switch View Mode
function setMode(mode) {
    currentMode = mode;
    ['fps', 'orbit', 'plan'].forEach(m => {
        const btn = document.getElementById(`btn-${m}`);
        if (btn) btn.classList.toggle('active', m === mode);
    });

    const fpsHUD = document.getElementById('fps-crosshair');
    const cutControl = document.getElementById('cut-height-control');
    const joystickEl = document.getElementById('virtual-joystick-container');
    const navHelp = document.getElementById('navigation-help');

    if (mode === 'orbit') {
        if (orbitControls) orbitControls.enabled = true;
        camera.position.set(0, 14, 16);
        if (orbitControls) {
            orbitControls.target.set(0, 1.2, 0);
            orbitControls.update();
        }
        if (fpsHUD) fpsHUD.style.display = 'none';
        if (cutControl) cutControl.style.display = 'flex';
        if (joystickEl) joystickEl.style.display = 'none';
        if (navHelp && !isMobile) navHelp.style.display = 'flex';
        
        const toggleLabels = document.getElementById('toggle-labels');
        labelsGroup.visible = toggleLabels ? toggleLabels.checked : true;

        const slider = document.getElementById('wall-height-slider');
        if (slider) setWallsHeight(slider.value);

    } else if (mode === 'plan') {
        if (orbitControls) orbitControls.enabled = true;
        camera.position.set(0, 22, 0.001);
        if (orbitControls) {
            orbitControls.target.set(0, 0, 0);
            orbitControls.update();
        }
        if (fpsHUD) fpsHUD.style.display = 'none';
        if (cutControl) cutControl.style.display = 'none';
        if (joystickEl) joystickEl.style.display = 'none';
        if (navHelp && !isMobile) navHelp.style.display = 'flex';

        const toggleLabels = document.getElementById('toggle-labels');
        labelsGroup.visible = toggleLabels ? toggleLabels.checked : true;

        setWallsHeight(1.2);

    } else if (mode === 'fps') {
        if (orbitControls) orbitControls.enabled = false;
        camera.position.copy(player.pos).add(apartmentGroup.position);
        updateCameraRotation();
        if (fpsHUD) fpsHUD.style.display = isMobile ? 'none' : 'block';
        if (cutControl) cutControl.style.display = 'none';
        if (joystickEl) joystickEl.style.display = isMobile ? 'block' : 'none';
        if (navHelp && !isMobile) navHelp.style.display = 'flex';

        // Hide room labels in First Person
        labelsGroup.visible = false;

        setWallsHeight(2.70);
    }

    updateCameraFov();
    updateNearestDoorHUD();

    if (isMobile) {
        closeSidebar();
    }
}

// Teleport to Room
function teleportTo(roomId) {
    const room = APARTMENT_DATA.rooms.find(r => r.id === roomId);
    if (!room) return;

    player.pos.set(room.spawn[0], player.height, room.spawn[2]);
    player.rotY = room.spawn[3];
    player.pitch = 0;

    if (currentMode !== 'fps') {
        setMode('fps');
    } else {
        camera.position.copy(player.pos).add(apartmentGroup.position);
        updateCameraRotation();
    }
    updateCurrentRoomDisplay();
    updateNearestDoorHUD();

    if (isMobile) {
        closeSidebar();
    }
}

// Wall Cut Height
function setWallsHeight(heightVal) {
    const h = parseFloat(heightVal);
    const valEl = document.getElementById('wall-height-val');
    if (valEl) valEl.innerText = `${h.toFixed(1)}m`;

    wallsGroup.children.forEach(wObj => {
        const baseH = wObj.userData.baseHeight || 2.70;
        const targetScaleY = Math.min(1.0, h / baseH);
        wObj.scale.y = targetScaleY;
    });

    pillarsGroup.children.forEach(pObj => {
        const baseH = pObj.userData.baseHeight || 2.70;
        pObj.scale.y = Math.min(1.0, h / baseH);
    });

    shaftsGroup.children.forEach(sObj => {
        const baseH = sObj.userData.baseHeight || 2.70;
        sObj.scale.y = Math.min(1.0, h / baseH);
    });

    const ceilCheckbox = document.getElementById('toggle-ceiling');
    ceilingGroup.visible = (h >= 2.65 && ceilCheckbox && ceilCheckbox.checked);
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
        if (k === 'e') triggerNearestDoor();
    });

    window.addEventListener('keyup', (e) => {
        const k = e.key.toLowerCase();
        if (k === 'w' || k === 'arrowup') keys.w = false;
        if (k === 'a' || k === 'arrowleft') keys.a = false;
        if (k === 's' || k === 'arrowdown') keys.s = false;
        if (k === 'd' || k === 'arrowright') keys.d = false;
        if (!e.shiftKey) keys.shift = false;
    });

    // Mouse Controls
    const canvas = renderer.domElement;
    canvas.addEventListener('mousedown', (e) => {
        if (isMeasuring) {
            handleMeasureClick(e);
            return;
        }

        const doorClicked = checkDoorClick(e.clientX, e.clientY);
        if (doorClicked) return;

        if (currentMode === 'fps') {
            isDraggingFPS = true;
            prevMousePos = { x: e.clientX, y: e.clientY };
            if (e.button === 0) {
                try { canvas.requestPointerLock?.(); } catch(_) {}
            }
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
                const sensitivity = 0.0022;
                player.rotY -= movementX * sensitivity;
                player.pitch -= movementY * sensitivity;
                player.pitch = Math.max(-Math.PI / 2.3, Math.min(Math.PI / 2.3, player.pitch));
                updateCameraRotation();
            }
        }
    });

    // Mobile Touch Controls
    setupTouchControls();
}

// Touch Controls
function setupTouchControls() {
    const canvas = renderer.domElement;
    let touchLookStart = { x: 0, y: 0 };
    let isLookingTouch = false;
    let touchStartTime = 0;

    canvas.addEventListener('touchstart', (e) => {
        if (e.touches.length === 0) return;
        touchStartTime = Date.now();

        if (currentMode === 'fps') {
            for (let i = 0; i < e.touches.length; i++) {
                const t = e.touches[i];
                if (t.clientX > window.innerWidth * 0.32) {
                    isLookingTouch = true;
                    touchLookStart = { x: t.clientX, y: t.clientY };
                    break;
                }
            }
        }
    }, { passive: true });

    canvas.addEventListener('touchmove', (e) => {
        if (currentMode === 'fps' && isLookingTouch) {
            for (let i = 0; i < e.touches.length; i++) {
                const t = e.touches[i];
                if (t.clientX > window.innerWidth * 0.32) {
                    const dx = t.clientX - touchLookStart.x;
                    const dy = t.clientY - touchLookStart.y;
                    touchLookStart = { x: t.clientX, y: t.clientY };

                    const sensitivity = 0.0035;
                    player.rotY -= dx * sensitivity;
                    player.pitch -= dy * sensitivity;
                    player.pitch = Math.max(-Math.PI / 2.3, Math.min(Math.PI / 2.3, player.pitch));
                    updateCameraRotation();
                    break;
                }
            }
        }
    }, { passive: true });

    canvas.addEventListener('touchend', (e) => {
        isLookingTouch = false;
        if (Date.now() - touchStartTime < 250 && e.changedTouches.length > 0) {
            const t = e.changedTouches[0];
            checkDoorClick(t.clientX, t.clientY);
        }
    }, { passive: true });

    setupVirtualJoystick();
}

function setupVirtualJoystick() {
    const zone = document.getElementById('joystick-zone');
    const knob = document.getElementById('joystick-knob');
    if (!zone || !knob) return;

    let touchId = null;

    zone.addEventListener('touchstart', (e) => {
        e.preventDefault();
        const t = e.changedTouches[0];
        touchId = t.identifier;
        const rect = zone.getBoundingClientRect();
        touchJoystick.active = true;
        touchJoystick.startX = rect.left + rect.width / 2;
        touchJoystick.startY = rect.top + rect.height / 2;
    }, { passive: false });

    zone.addEventListener('touchmove', (e) => {
        e.preventDefault();
        if (!touchJoystick.active) return;
        for (let i = 0; i < e.changedTouches.length; i++) {
            const t = e.changedTouches[i];
            if (t.identifier === touchId) {
                const dx = t.clientX - touchJoystick.startX;
                const dy = t.clientY - touchJoystick.startY;
                const maxR = 38;
                const dist = Math.hypot(dx, dy);
                const angle = Math.atan2(dy, dx);
                const clampedR = Math.min(dist, maxR);

                const kx = Math.cos(angle) * clampedR;
                const ky = Math.sin(angle) * clampedR;
                knob.style.transform = `translate(${kx}px, ${ky}px)`;

                touchJoystick.moveX = kx / maxR;
                touchJoystick.moveZ = ky / maxR;
                break;
            }
        }
    }, { passive: false });

    const endHandler = (e) => {
        for (let i = 0; i < e.changedTouches.length; i++) {
            if (e.changedTouches[i].identifier === touchId) {
                touchJoystick.active = false;
                touchJoystick.moveX = 0;
                touchJoystick.moveZ = 0;
                knob.style.transform = 'translate(0px, 0px)';
                touchId = null;
                break;
            }
        }
    };

    zone.addEventListener('touchend', endHandler, { passive: true });
    zone.addEventListener('touchcancel', endHandler, { passive: true });
}

// Window Resize & Dynamic FOV update
function onWindowResize() {
    if (!camera || !renderer) return;
    camera.aspect = window.innerWidth / window.innerHeight;
    updateCameraFov();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

// First Person Movement with Natural Stride Pace
function updateFPSMovement(dt) {
    if (currentMode !== 'fps') return;

    let moveX = 0;
    let moveZ = 0;

    if (keys.w) moveZ -= 1;
    if (keys.s) moveZ += 1;
    if (keys.a) moveX -= 1;
    if (keys.d) moveX += 1;

    if (touchJoystick.active) {
        moveX += touchJoystick.moveX;
        moveZ += touchJoystick.moveZ;
    }

    if (moveX !== 0 || moveZ !== 0) {
        const len = Math.hypot(moveX, moveZ);
        if (len > 1.0) {
            moveX /= len;
            moveZ /= len;
        }

        const currentSpeed = keys.shift ? player.speed * player.sprintMultiplier : player.speed;
        const forward = new THREE.Vector3(0, 0, -1).applyAxisAngle(new THREE.Vector3(0, 1, 0), player.rotY);
        const right = new THREE.Vector3(1, 0, 0).applyAxisAngle(new THREE.Vector3(0, 1, 0), player.rotY);

        const deltaMove = new THREE.Vector3()
            .addScaledVector(forward, -moveZ * currentSpeed * dt)
            .addScaledVector(right, moveX * currentSpeed * dt);

        const targetX = player.pos.x + deltaMove.x;
        const targetZ = player.pos.z + deltaMove.z;

        const boundedX = Math.max(0.60, Math.min(13.15, targetX));
        const boundedZ = Math.max(0.60, Math.min(10.80, targetZ));

        player.pos.x = boundedX;
        player.pos.z = boundedZ;
        player.pos.y = player.height;

        camera.position.copy(player.pos).add(apartmentGroup.position);
        updateCurrentRoomDisplay();
    }

    updateNearestDoorHUD();
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

    minimapCanvas.addEventListener('click', (e) => {
        const rect = minimapCanvas.getBoundingClientRect();
        const mx = e.clientX - rect.left;
        const my = e.clientY - rect.top;

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

    const px = player.pos.x * scaleX;
    const pz = player.pos.z * scaleY;

    // FOV cone
    ctx.fillStyle = 'rgba(197, 168, 130, 0.35)';
    ctx.beginPath();
    ctx.moveTo(px, pz);
    const fovAngle = 0.55;
    ctx.arc(px, pz, 20, -player.rotY - Math.PI / 2 - fovAngle, -player.rotY - Math.PI / 2 + fovAngle);
    ctx.closePath();
    ctx.fill();

    // Player dot
    ctx.fillStyle = '#c5a882';
    ctx.beginPath();
    ctx.arc(px, pz, 4, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 1.5;
    ctx.stroke();
}

// Measuring Tool
function toggleMeasure() {
    isMeasuring = !isMeasuring;
    const btn = document.getElementById('btn-measure');
    if (btn) btn.classList.toggle('active', isMeasuring);

    const info = document.getElementById('measure-info');
    if (info) info.style.display = isMeasuring ? 'block' : 'none';

    if (!isMeasuring) clearMeasure();
}

function handleMeasureClick(e) {
    const mouse = new THREE.Vector2(
        (e.clientX / window.innerWidth) * 2 - 1,
        -(e.clientY / window.innerHeight) * 2 + 1
    );

    const raycaster = new THREE.Raycaster();
    raycaster.setFromCamera(mouse, camera);

    const intersects = raycaster.intersectObjects([...floorsGroup.children, ...wallsGroup.children, ...pillarsGroup.children, ...fixturesGroup.children], true);
    if (intersects.length > 0) {
        const pt = intersects[0].point;
        measurePoints.push(pt);

        const dotGeo = new THREE.SphereGeometry(0.08, 10, 10);
        const dotMat = new THREE.MeshBasicMaterial({ color: 0xff3344 });
        const dotMesh = new THREE.Mesh(dotGeo, dotMat);
        dotMesh.position.copy(pt);
        scene.add(dotMesh);

        if (measurePoints.length === 2) {
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

// Sidebar Drawer Toggle for Mobile
function toggleSidebar() {
    const aside = document.querySelector('aside');
    if (aside) aside.classList.toggle('open');
}

function closeSidebar() {
    const aside = document.querySelector('aside');
    if (aside) aside.classList.remove('open');
}

// Animation Loop: Smooth Interactive Door Swings
function animate() {
    requestAnimationFrame(animate);

    if (!clock) return;
    const dt = Math.min(clock.getDelta(), 0.1);

    interactiveDoors.forEach(d => {
        if (Math.abs(d.currentAngle - d.targetAngle) > 0.001) {
            d.currentAngle = THREE.MathUtils.lerp(d.currentAngle, d.targetAngle, dt * 7.5);
            d.pivot.rotation.y = d.currentAngle;
        }
    });

    if (currentMode === 'orbit' || currentMode === 'plan') {
        if (orbitControls) orbitControls.update();
    } else if (currentMode === 'fps') {
        updateFPSMovement(dt);
    }

    renderMinimap();
    if (renderer && scene && camera) {
        renderer.render(scene, camera);
    }
}

// Expose functions to window
window.setMode = setMode;
window.teleportTo = teleportTo;
window.setWallsHeight = setWallsHeight;
window.setupLighting = setupLighting;
window.setObserverHeight = setObserverHeight;
window.toggleDoor = toggleDoor;
window.triggerNearestDoor = triggerNearestDoor;
window.toggleCeiling = function(checked) { ceilingGroup.visible = checked; };
window.toggleOverlay = function(checked) { if (floorPlanMesh) floorPlanMesh.visible = checked; };
window.toggleLabels = function(checked) { if (currentMode !== 'fps') labelsGroup.visible = checked; };
window.toggleMeasure = toggleMeasure;
window.toggleSidebar = toggleSidebar;
window.closeSidebar = closeSidebar;

// Boot
window.addEventListener('DOMContentLoaded', init);
