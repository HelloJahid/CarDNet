import torch
from torch import nn
from torch.nn import functional as F


class ChannelAttention(nn.Module):
    def __init__(self, in_channel):
        super(ChannelAttention, self).__init__()
        self.pool_h = nn.AdaptiveAvgPool2d((None, 1))
        self.conv1 = nn.Conv2d(in_channel, in_channel, kernel_size=(3, 1), padding=(1, 0), bias=False)
        self.bn1 = nn.BatchNorm2d(in_channel)

        self.pool_v = nn.AdaptiveAvgPool2d((1, None))
        self.conv2 = nn.Conv2d(in_channel, in_channel, kernel_size=(1, 3), padding=(0, 1), bias=False)
        self.bn2 = nn.BatchNorm2d(in_channel)


    def forward(self, x):
        x1 = self.pool_h(x)
        x1 = self.conv1(x1)
        x1 = self.bn1(x1)

        x2 = self.pool_v(x)
        x2 = self.conv2(x2)
        x2 = self.bn2(x2)

        return x1, x2


class SpatialAttention(nn.Module):
    def __init__(self, kernel_size=7):
        super(SpatialAttention, self).__init__()
        self.dilated_conv_1 = nn.Conv2d(in_channels=2, out_channels=1, kernel_size=3, padding=2, dilation=2, bias=False)
        self.dilated_conv_2 = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3, padding=2, dilation=2, bias=False)
        self.bn1 = nn.BatchNorm2d(1)

    def forward(self, x):
        idnetity = x
        avg_out = torch.mean(x, dim=1, keepdim=True)
        max_out, _ = torch.max(x, dim=1, keepdim=True)
        combined = torch.cat([avg_out, max_out], dim=1)
        dilated_1 = self.dilated_conv_1(combined)
        dilated_2 = self.dilated_conv_2(dilated_1)

        spatial_attention =  self.bn1(dilated_2)
        return spatial_attention



class CAM_MODULE(nn.Module):
    def __init__(self, in_channels, kernel_size=7):
        super(CAM_MODULE, self).__init__()
        self.channel_attention = ChannelAttention(in_channels)
        self.spatial_attention = SpatialAttention(kernel_size)

    def forward(self, x):
        h, w = self.channel_attention(x)
        c = self.spatial_attention(x)

        fusion = torch.sigmoid(w + h + c)

        residual_fusion = x * fusion
        cam_attn = residual_fusion + x

        return cam_attn

# Example usage:
input_channels = 256
input_tensor = torch.randn(32, input_channels, 32, 32)
cam_out = CAM_MODULE(input_channels)
output_tensor = cam_out(input_tensor)

print(output_tensor.shape, input_tensor.shape)
