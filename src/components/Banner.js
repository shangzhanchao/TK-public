import { defineComponent, ref, onMounted } from 'vue';

export default defineComponent({
  name: 'BannerSection',
  setup() {
    const images = ref([
      { id: 1, src: 'https://via.placeholder.com/1200x400?text=机器人+1' },
      { id: 2, src: 'https://via.placeholder.com/1200x400?text=机器人+2' },
      { id: 3, src: 'https://via.placeholder.com/1200x400?text=机器人+3' }
    ]);
    const current = ref(0);

    onMounted(() => {
      setInterval(() => {
        current.value = (current.value + 1) % images.value.length;
      }, 5000);
    });

    return { images, current };
  },
  template: `
    <div class="relative w-full overflow-hidden">
      <div v-for="(img, index) in images" :key="img.id" class="absolute inset-0 transition-opacity" :class="{ 'opacity-0': index !== current, 'opacity-100': index === current }">
        <img :src="img.src" class="w-full h-60 md:h-96 object-cover" alt="banner" />
      </div>
    </div>
  `
});
