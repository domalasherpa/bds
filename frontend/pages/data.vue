<script setup lang="ts">
import { doc, getDoc, getFirestore } from 'firebase/firestore';

const db = getFirestore();
const docRef= doc(db, "log", "test");
const docSnap = await getDoc(docRef);

</script>
<template>
    <div>
        {{ docSnap.data() }}    
    </div>

</template>