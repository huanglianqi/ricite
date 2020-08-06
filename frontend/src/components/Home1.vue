<template>
  <div
    id="home">
    <canvas
      id="cube">
    </canvas>
  </div>
</template>

<script>
import * as THREE from 'three'
import {OrbitControls} from 'three/examples/jsm/controls/OrbitControls'
// import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader'

export default {
  name: 'home',
  data () {
    return {
      canvas: null,
      cube: null,
      renderer: null,
      scene: null,
      camera: null,
      cameraX: 0,
      cameraY: 0,
      cameraZ: 5,
      fov: 75,
      near: 0.1,
      far: 1000,
      light: null,
      lightTX: 0,
      lightTY: 5,
      lightTZ: -5,
      lightX: 0,
      lightY: 10,
      lightZ: 0,
      controls: null
    }
  },
  methods: {
    init () {
      this.canvas = document.getElementById('cube')
      this.createScene()
      this.createCamera()
      this.createRenderer()
      this.createControls()
      this.createLights()
      this.createMeshes()
    },
    createScene () {
      this.scene = new THREE.Scene()
      this.scene.background = new THREE.Color(0xffffff)
    },
    createCamera () {
      this.camera = new THREE.PerspectiveCamera(
        this.fov,
        this.canvas.clientWidth / this.canvas.clientHeight,
        this.near,
        this.far
      )
      this.camera.position.set(
        this.cameraX,
        this.cameraY,
        this.cameraZ
      )
    },
    createLights () {
      this.light = new THREE.DirectionalLight(0xffffff, 1)
      this.light.position.set(
        this.lightX,
        this.lightY,
        this.lightZ
      )
      this.light.target.position.set(
        this.lightTX,
        this.lightTY,
        this.loghtTZ
      )
      this.scene.add(this.light)
    },
    createMeshes () {
      const geometry = new THREE.BoxBufferGeometry(
        this.cubeX,
        this.cubeY,
        this.cubeZ
      )
      const material = new THREE.MeshLambertMaterial({color: 0x44aa88})
      this.cube = new THREE.Mesh(geometry, material)
      this.scene.add(this.cube)
    },
    createRenderer () {
      this.renderer = new THREE.WebGLRenderer(
        {
          canvas: this.canvas,
          antialias: true
        }
      )
      this.renderer.setSize(
        this.canvas.clientWidth,
        this.canvas.clientHeight,
        true
      )
      this.renderer.setPixelRatio(window.devicePixelRatio)
    },
    createControls () {
      this.controls = new OrbitControls(this.camera, this.renderer.domElement)
      this.controls.target.set(0, 0, 0)
      this.controls.update()
    },
    update () {
      this.cube.rotation.x += 0.005
      this.cube.rotation.y += 0.005
      this.cube.rotation.z += 0.005
      this.controls.update()
    },
    play () {
      this.renderer.setAnimationLoop(
        () => {
          this.update()
          this.render()
        }
      )
    },
    stop () {
      this.renderer.setAnimationLoop(null)
    },
    render () {
      this.renderer.render(this.scene, this.camera)
    },
    onWindowResize () {
      // this.camera.aspect = this.canvas.clientWidth / this.canvas.clientHeight
      // this.camera.updateProjectionMatrix()
      // this.renderer.setSize(this.canvas.clientWidth, this.canvas.clientHeight)
      console.log('resize windows')
    }
  },
  created () {
    window.addEventListener(
      'resize',
      this.onWindowResize(),
      false
    )
  },
  mounted () {
    this.init()
    this.play()
  },
  destroyed () {
    window.removeEventListener(
      'resize',
      this.onWindowResize(),
      false
    )
  }
}
</script>

<style>
body {
  margin: 0;
}
canvas {
  display: block;
}
#cube {
  width: 100%;
  height: 100%;
}
</style>
