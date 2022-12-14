# Dual-Booting Ubuntu 22.04 #
Dual booting ubuntu into my zenbook pro duo running windows 11 was both an hectic at the same time interesting task for me. The fact that ubuntu runs soo smooth on my i7 9th gen processor without any error made my day. Though i had to face several issues while installing ubuntu from almost loosing my windows and data to a point i almost lost my hope, I didnt gave up. 

## Problems you may face ##
- While dual booting ubuntu, make sure to disable the bitlocker on the drive you are planning to install ubuntu
- Also disable Intel RST in your SATA configuration. Use AHCI or any other settings.
- If you suddenly change from Intel RST to AHCL, your windows may crash.
- Watch this [page](https://www.partitionwizard.com/partitionmagic/enable-ahci-after-win-10-installation.html) to correctly configure windows for AHCI

