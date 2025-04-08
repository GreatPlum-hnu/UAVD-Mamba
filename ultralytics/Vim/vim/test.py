from models_mamba import VisionMamba
import torch

def test():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = VisionMamba(
        patch_size=16,
        embed_dim=192,
        depth=24,
        rms_norm=True,
        residual_in_fp32=True,
        fused_add_norm=True,
        final_pool_type='mean',
        if_abs_pos_embed=True,
        if_rope=False,
        if_rope_residual=False,
        bimamba_type="V2",
        if_cls_token=True,
        if_divide_out=True,
        use_double_cls_token=True
    ).to(device)
 
    x = torch.randn(size=(4,3,224,224)).to(device)
    preds = model(x)
    print(preds.shape)
 
if __name__ == '__main__':
    test()