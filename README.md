# carDNet

The proposed CarDNet model includes two main parts: ResNet50 and an enhanced version of the attention net module. The key innovation is a refined attention module known as CAM (Convolutional Attention Module), aimed at better detecting damage between different classes. CAM consists of two parallel sub-modules: one for channels and one for spatial features. Placed after each residual block in the ResNet50 network, the CAM module dynamically enhances each incoming intermediate feature.


![Example Image](utils/cam.jpeg)


# CarDNet: CNN-Attention Based Car Damage Classification Network  

The rapid growth of online used car marketplaces highlights the need for **accurate and reliable car damage classification** to ensure fair pricing and customer trust. Traditional manual inspections are subjective, time-consuming, and error-prone. While CNN-based approaches have been widely adopted, they often fail to capture contextual dependencies in complex car images, leading to confusion between damaged and undamaged regions.  

To address these challenges, we propose **CarDNet**, a CNN-Attention based network enhanced by a **Convolutional Attention Module (CAM)**. CarDNet integrates **channel and spatial attention branches** within CNNs to improve feature extraction, highlight relevant regions, and enhance overall classification accuracy.  

---

##  Key Contributions  

1. **High-Quality Dataset**  
   - Curated a diverse, annotated, and balanced dataset combining **Carsales private data** and the public **CarDD dataset**.  
   - Six categories: dent, scratch, glass shatter, tire flat, lamp broken, and no damage.  
   - Applied systematic augmentation to reach **5000+ images per class**.  

2. **Convolutional Attention Module (CAM)**  
   - Lightweight and seamlessly integrates with CNNs.  
   - Combines **channel attention** (what features to focus on) and **spatial attention** (where to focus).  
   - Enables differentiation between subtle damages and irrelevant artefacts (e.g., reflections, shadows).  

3. **Integration with Pretrained CNNs**  
   - Experimented with **ResNet50, VGG16, and DenseNet121**.  
   - Chose **ResNet50 + CAM** as the backbone for superior performance.  

4. **Robust Evaluation**  
   - Benchmarked against **eight state-of-the-art attention mechanisms** (SeNet, SRM, Gate, GCNet, CCNet, BAM, Coordinate, SPNet).  
   - Performed **ablation studies** showing both channel and spatial branches significantly boost accuracy.  

5. **Practical Impact**  
   - Seamless integration into **Carsales AI engine**, improving real-time classification of car damages.  
   - Benefits **used-car pricing accuracy**, insurance transparency, and customer satisfaction.  

---

##  Results  

- **Validation Accuracy:** 98.56%  
- **Test Accuracy:** 97%  
- **Precision:** 97.0%  
- **Recall:** 96.8%  
- **F1 Score:** 96.9%  

---

##  Model Architecture  

<p align="center">
  <img src="utils/cam.jpeg" alt="CarDNet Architecture" width="600">
</p>  

*Figure: Overview of CarDNet with integrated Convolutional Attention Module (CAM).*  

---

---

## 🙏 Acknowledgements  

We gratefully acknowledge the support of our collaborators and partners:  

- [**Carsales.com Ltd**](https://www.carsales.com.au/)  Providing industry dataset access and invaluable guidance.  

- [**CarDD Dataset**](https://cardd-ustc.github.io/)  Offering a public benchmark for rigorous evaluation.  

- [**RMIT Enterprise AI and Data Analytics Hub**  ](https://rmit-aihub.org.au/) For experimental environments, recommendations, and research insights.  

---

