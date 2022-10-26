_base_ = ['./oriented_rcnn_r50_fpn_1x_fair1m_le90.py']
model = dict(
    type='OrientedRCNNLFCP',
    backbone=dict(
        type='LowlResNet',
        frozen_stages=-1),
    neck=dict(
        type='LFCP',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        num_outs=5,
        start_level=0,
        end_level=-1,
        norm_cfg=None,
        act_cfg=None,
        upsample_cfg=dict(
            type='carafe',
            up_kernel=5,
            up_group=1,
            encoder_kernel=5,
            encoder_dilation=1,
            compressed_channels=256)),
    rpn_head=dict(
        start_level=1,
        anchor_generator=dict(
            strides=[4, 8, 16, 32]
        )),
    roi_head=dict(
        bbox_roi_extractor=dict(
            featmap_strides=[2, 4, 8, 16])),
)

data = dict(
    samples_per_gpu=1)
optimizer = dict(lr=0.01)
