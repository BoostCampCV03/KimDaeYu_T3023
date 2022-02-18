from CycleGAN import *
import matplotlib.pyplot as plt
from PIL import Image
from torchvision.transforms import ToTensor, ToPILImage

cuda = torch.cuda.is_available()
Tensor = torch.cuda.FloatTensor if cuda else torch.Tensor
G_AB, G_BA = torch.load("./weights/G_AB.pt"), torch.load("./weights/G_BA.pt")


def sample_images(real_A, real_B, figside=1.5):
    assert real_A.size() == real_B.size(), 'The image size for two domains must be the same'
    
    G_AB.eval()
    G_BA.eval()
    real_A = ToTensor(real_A)
    real_B = ToTensor(real_B)
    #real_A = real_A.type(Tensor)
    fake_B = G_AB(real_A).detach()
    #real_B = real_B.type(Tensor)
    fake_A = G_BA(real_B).detach()
    
    nrows = real_A.size(0)
    real_A = make_grid(real_A, nrow=nrows, normalize=True)
    fake_B = make_grid(fake_B, nrow=nrows, normalize=True)
    real_B = make_grid(real_B, nrow=nrows, normalize=True)
    fake_A = make_grid(fake_A, nrow=nrows, normalize=True)
    
    image_grid = torch.cat((real_A, fake_B, real_B, fake_A), 1).cpu().permute(1, 2, 0)
    
    plt.figure(figsize=(figside*nrows, figside*4))
    plt.imshow(image_grid)
    plt.axis('off')
    plt.show()


file_A = os.path.join("./" + "3.jpg")
print(file_A)
img_A = Image.open(file_A)
# real_A = img_A.type(Tensor)
plt.figure()
plt.imshow(img_A)
#sample_images()

#file = 

    #     if mode == 'train':
    #         self.files_A = [os.path.join(A_dir, name) for name in sorted(os.listdir(A_dir))[:250]]
    #         self.files_B = [os.path.join(B_dir, name) for name in sorted(os.listdir(B_dir))[:250]]
    #     elif mode == 'test':
    #         self.files_A = [os.path.join(A_dir, name) for name in sorted(os.listdir(A_dir))[250:]]
    #         self.files_B = [os.path.join(B_dir, name) for name in sorted(os.listdir(B_dir))[250:301]]
        
    #     self.transforms = transforms
        
    # def __len__(self):
    #     return len(self.files_A)
    
    # def __getitem__(self, index):
    #     file_A = self.files_A[index]