import { defineComponent } from 'vue';

export default defineComponent({
  name: 'ProductCard',
  props: {
    product: Object
  },
  template: `
    <div class="border rounded-lg p-4 hover:shadow-lg transition">
      <img :src="product.img" class="w-full h-40 object-cover" alt="product" />
      <h3 class="mt-2 font-semibold">{{ product.name }}</h3>
      <p class="text-sm text-gray-500">{{ product.desc }}</p>
      <div class="mt-2 flex justify-between items-center">
        <span class="text-blue-600 font-bold" v-if="product.price">¥{{ product.price }}</span>
        <button class="bg-blue-600 text-white px-3 py-1 rounded" v-else>立即咨询</button>
        <button class="text-gray-500 hover:text-red-500" title="收藏">♥</button>
      </div>
    </div>
  `
});
