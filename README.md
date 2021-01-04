# Photometric-Stereo
# (Shape from Shading algorithm)  
  
  
Input: a set of photographs of a static scene taken with known lighting directions  
Output: albedo (paint), normal directions, and the height map  

*Slides are credited to Subhransu Maji, associate professor in the College of Information and Computer Sciences at the University of Massachusetts, Amherst.*
![Example](demos/photo-example01.png)  
![Example](demos/photo-example02.png)  
![Example](demos/photo-example03.png)  


## Compute the surface height map by integration
- ### Method 1: Integrating first the rows, then the columns  
![Example](demos/photo-height-row.png)  
---
- ### Method 2: Integrating first the columns, then the rows  
![Example](demos/photo-height-col.png)  
---
- ### Method 3: Average of method 1 and 2  
![Example](demos/photo-height-colrowavg.png)  
---
- ### Method 4: Average of multiple **random paths**  
![Example](demos/photo-height-random03.png)  
![Example](demos/photo-height-random30.png)  




