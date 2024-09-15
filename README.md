# MBR (Master Boot Record)

## 1. Summary
Master Boot Record is a partition scheme that was used on older operating systems like Windows 2000-8.1. Some machines of windows 10 might use that but majorly new systems use GUID Partioning Table(GPT) partitioning scheme. It is used for hard drives that are of maximum 2 TB size and can host a maximum of 26 partitions (engilsh alphabet A-Z). 3 partitions are **primary** and the fourth partition is extended partition that hosts the remaining 23 partitions if created that are called **Logical Partitions**.

The MBR (which is always located on the first sector of a hard disk) contains that disk's Master (or Primary) Partition Table; often the only partition table on many PCs today. The partition table comprises only 12.5% (64 bytes) of this 512-byte sector
Basic structure of the Master Boot Record is:

| Offsets (Decimal) | Offsets (Hex)  | Length (Bytes) | Description              |
|-------------------|----------------|----------------|--------------------------|
| 000 - 445         | 000 - 1BD      | 446            | Code Area                |
| 446 - 509         | 1BE - 1FD      | 64             | Master Partition Table    |
| 510 - 511         | 1FE - 1FF      | 2              | Boot Record Signature     |

Boot Record signature; sometimes called its Magic number, and often expressed as the 16-bit hexadecimal Word, 0xAA55 (or: AA55h) for the *little-endian*.

![{BA83B76D-54F0-491A-A15A-C0F5DBBB8085}](https://github.com/user-attachments/assets/cf9d38fe-853d-4662-81e7-a30028b1e39b)

**BLUE: Bootable code**

**GREEN: Partition table**

**YELLOW: Boot Record signature**

## 2. Partitions
This standard MBR structure has always contained a Partition Table with four 16-byte entries as follows:
| Offsets (within MBR sector) | Length (in bytes) | Contents                              |
|-----------------------------|-------------------|---------------------------------------|
| Decimal    | Hex             |                   |                                       |
|------------|-----------------|-------------------|---------------------------------------|
| 446 - 461  | 1BE - 1CD       | 16                | Table Entry for Primary Partition #1  |
| 462 - 477  | 1CE - 1DD       | 16                | Table Entry for Primary Partition #2  |
| 478 - 493  | 1DE - 1ED       | 16                | Table Entry for Primary Partition #3  |
| 494 - 509  | 1EE - 1FD       | 16                | Table Entry for Primary Partition #4  |

Thus, disks using this standard table can have no more than four Primary partitions, or as described earlier, up to three Primary partitions plus one Extended partition.
The general format for entries within their partition tables:
| Relative Offsets (within entry) | Length (bytes) | Contents                        |
|---------------------------------|----------------|---------------------------------|
| 0                               | 1              | Boot Indicator (80h = active)   |
| 1 - 3                           | 3              | Starting CHS values             |
| 4                               | 1              | Partition-type                  |
| 5 - 7                           | 3              | Ending CHS values               |
| 8 - 11                          | 4              | Starting Sector                 |
| 12 - 15                         | 4              | Partition Size (in sectors)     |

These areas are also highlited on the image attached below:

![image](https://github.com/user-attachments/assets/67a1e319-d9fe-425f-bf5f-a689e724f187)

Since disk editors often display 16 bytes per line starting with offset 000 and partition tables begin at offset 1BEh within these sectors, it's highly likely you'll see the entries overlapping each display line.

## 3. Decoding Table Entry
1. **Boot Indicator** In this case, it's 80h, but you'll rarely, if ever, see anything except 00h in Extended Boot Records. Technically, only the "Active" (bootable) Primary partition is ever supposed to have its 'high bit' set (making that byte, 80h). Some boot managers might allow logical partitions to be set active, but more likely a boot manager will never use this indicator when doing so.

2. **Starting Sector** in CHS values (3 bytes). These values pinpoint the location of a partition's first sector, if  it's within the first 1024 cylinders of a hard disk. When a sector is beyond that point, the CHS tuples are normally set to their maximum allowed values of 1023, 254, 63; which stand for the 1024th cylinder, 255th head and 63rd sector, due to the fact, cylinder and head counts begin at zero. These values appear on the disk as the three bytes: FE FF FF (in that order).

*Note: These bytes are somewhat in the order of Head, Sector and Cylinder, but the cylinder value requires more than 8-bits (one byte) and the sector value uses less than 8-bits, making this conversion rather difficult at times. The 01 01 00 in our example above, stands for CHS (0, 1, 1)  or LBA Sector 63; the 64th sector on the disk, since its count begins at LBA 0 [4]. The 3-byte Ending CHS values will be dealt with in detail under the Decoding CHS Values section below.*

3. **Partition Type Descriptor** Its single byte allows for only 256 possible values to indicate all types of partitions that can exist under the DOS/Basic Disk partitioning scheme. In this case, 0Bh, indicates a FAT32 file system. Refer partition types below

4. **Ending Sector** in CHS values (3 bytes); 1F 3F 33 in our example above. Refer next section of decoding CHS Values.

5. **Starting Sector** (4 bytes). LBA (Absolute Sector) value. This value uniquely identifies the first sector of a partition just as Starting CHS values do. But it does so by using a 4-byte Logical Block Address (starts counting from Absolute Sector 0), which means it can locate the beginning of a partition within the first  FFFF FFFFh or 4,294,967,296 sectors, for hard disks up to about 2,199,023,255,552 bytes (exactly 2,048 GiB)!

*Well, if that's true, then why did many computers have a limit problem at about 137 GB? Because many BIOS chips use only 28-bits for this value (a Hexadecimal number of FFF FFFFh or exactly 128 GiB) instead of the 32-bits used by partition tables! See 6 to 64 Bits: Hexadecimal Numbers Significant to Drive/Partition Limits for more details.*

*When you obtain all 4 bytes of this value (as stored on a little-endian computer), the byte-order must first be reversed. So, for our example above, the: 3F 00 00 00, becomes only: 3F hex. This means that our first (and ony) partition begins at Absolute Sector 3Fh, which is also LBA 63 (or the 64th sector on the disk). This is the first possible boot sector for any drive having 63 sectors per head/track.*

6. **Partition Size in Total sectors (4 bytes)**. As with the Starting Sector values, these four bytes allow for a number up to 2,048 GB for the size of each partition, and are also stored on disk in little-endian. So the stored bytes, 41 99 01 00, become: 19941 hex, for a size of: 104,769 sectors, or at 512 bytes/sector that's: 53,641,728 bytes (or only about 51 MB).

## 4. Decoding CHS Values

Although a Head number is fairly easy to compute (it's always whatever value [plus 1] is in the first byte of either the CHS Starting or Ending 3-byte fields), the Sector and Cylinder numbers are encoded into an odd arrangement of 6-bits and 10-bits, respectively, within the second and third bytes; making them more difficult to work with. The following diagram, attempts to make both the layout of a 3-byte CHS tuple and how to decode its numbers.

![image](https://github.com/user-attachments/assets/66f22bb8-e1fd-40da-be49-8db4957b12be)

A 3-byte CHS field encodes Cylinder (10-bits), Head (8-bits) and Sector (6-bits) values.

How to decode the three CHS bytes: The 8 bits (1111 1110) shown in the "Head" byte equal FE in hexadecimal (or 254). Since their count begins with Head 0, this refers to its 255th head. The "Sector" value is computed from the first six bits (starting with the least-significant bit, bits 0 through 5). Thus, the second CHS byte (BFh) yields: Sector 3Fh (or 63); from the bits: 11 1111.

The Cylinder value, which is 10 bits in length, receives its two most-significnat bits (10, in this case) from those of the second CHS byte (1011 1111 = BFh), but retains the original third byte (D3h, in this case) as its lowest 8 bits. The result, 10 1101 0011, gives us 2D3h, or 723, as the Cylinder value. Thus, the CHS tuple in the diagram above, for some partition's Ending Sector is: (723, 254, 63).

## 5. Partition Types

| Hex Code | Description                                                                                                                                                 |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 00       | Should NOT be used in an actual table entry! It does not indicate an unknown type, but rather an empty entry; in which case, all other fields should be zero |
| 01       | 12-bit FAT (on hard disks, not floppy disks, so you'll rarely see this today).                                                                              |
| 02       | XENIX root                                                                                                                                                  |
| 03       | XENIX /usr (obsolete)                                                                                                                                       |
| 04       | 16-bit FAT, partition; of sizes less than 32 MB.                                                                                                            |
| 05       | Extended Partition; within the first 1024 cylinders of a disk drive.                                                                                        |
| 06       | 16-bit FAT, partition; greater than or equal to 32 MB.                                                                                                      |
| 07       | Installable file systems: HPFS or NTFS. Also, QNX and Advanced Unix.                                                                                        |
| 08       | AIX bootable partition, AIX (Linux), SplitDrive, OS/2 (v1.3), Dell partition spanning multiple drives, Commodore DOS.                                       |
| 09       | AIX data partition, AIX bootable (Linux), Coherent file system, QNX.                                                                                        |
| 0A       | Coherent swap partition, OPUS or OS/2 Boot Manager.                                                                                                         |
| 0B       | 32-bit FAT                                                                                                                                                  |
| 0C       | 32-bit FAT, using INT 13 Extensions.                                                                                                                        |
| 0E       | 16-bit FAT >= 32 MB, using INT 13 Extensions.                                                                                                               |
| 0F       | Extended Partition, using INT 13 Extensions; often begins past cylinder 1024.                                                                               |
| 10       | OPUS                                                                                                                                                        |
| 11       | Hidden 12-bit FAT.                                                                                                                                          |
| 12       | Compaq diagnostics.                                                                                                                                        |
| 14       | Hidden 16-bit FAT, partition <32 MB, Novell DOS 7.0, AST DOS with logical sectored FAT.                                                                     |
| 16       | Hidden 16-bit FAT, partition >= 32 MB                                                                                                                       |
| 17       | Hidden IFS (HPFS, NTFS).                                                                                                                                    |
| 18       | AST Windows swap file                                                                                                                                       |
| 19       | Willowtech Photon coS                                                                                                                                       |
| 1B       | Hidden 32-bit FAT                                                                                                                                           |
| 1C       | Hidden 32-bit FAT, Ext INT 13                                                                                                                               |
| 1E       | Hidden 16-bit FAT >32 MB, Ext. INT 13 (PowerQuest specific)                                                                                                |
| 20       | Willowsoft Overture File System (OFS1)                                                                                                                      |
| 21       | Reserved (HP Volume Expansion, SpeedStor variant), Oxygen FSo2                                                                                              |
| 22       | Oxygen Extended                                                                                                                                             |
| 23       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 24       | NEC MS-DOS 3.x                                                                                                                                              |
| 26       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 31       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 33       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 34       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 36       | Reserved (HP Volume Expansion, SpeedStor variant?)                                                                                                          |
| 38       | Theos                                                                                                                                                       |
| 3C       | PowerQuest Files Partition Format                                                                                                                           |
| 3D       | Hidden NetWare                                                                                                                                              |
| 40       | VENIX 80286                                                                                                                                                 |
| 41       | Personal RISC Boot, PowerPC boot partition, PTS-DOS 6.70, Minix and DR-DOS.                                                                                 |
| 42       | Secure File System, Windows 2000/XP (NT 5): Dynamic extended partition, PTS-DOS 6.70, DR-DOS swap.                                                          |
| 43       | Alternative Linux native file system (EXT2fs), PTS-DOS 6.70, DR-DOS                                                                                         |
| 45       | Priam, EUMEL/Elan                                                                                                                                           |
| 46       | EUMEL/Elan                                                                                                                                                  |
| 47       | EUMEL/Elan                                                                                                                                                  |
| 48       | EUMEL/Elan                                                                                                                                                  |
| 4A       | ALFS/THIN lightweight filesystem for DOS                                                                                                                    |
| 4D       | QNX                                                                                                                                                         |
| 4E       | QNX                                                                                                                                                         |
| 4F       | QNX, Oberon boot/data partition                                                                                                                             |
| 50       | Ontrack Disk Manager, read-only partition, FAT partition                                                                                                    |
| 51       | Ontrack Disk Manager, read/write partition, FAT partition                                                                                                   |
| 52       | CP/M, Microport System V/386                                                                                                                                |
| 53       | Ontrack Disk Manager, write-only                                                                                                                            |
| 54       | Ontrack Disk Manager 6.0 (DDO)                                                                                                                              |
| 55       | EZ-Drive 3.05                                                                                                                                               |
| 56       | Golden Bow VFeature                                                                                                                                        |
| 5C       | Priam EDISK                                                                                                                                                 |
| 61       | Storage Dimensions SpeedStor                                                                                                                                |
| 63       | GNU HURD, Mach, MtXinu BSD 4.2 on Mach, Unix Sys V/386, 386/ix                                                                                              |
| 64       | Novell NetWare 286, SpeedStore                                                                                                                              |
| 65       | Novell NetWare (3.11 and 4.1)                                                                                                                               |
| 66       | Novell NetWare 386                                                                                                                                          |
| 67       | Novell NetWare                                                                                                                                              |
| 68       | Novell NetWare                                                                                                                                              |
| 69       | Novell NetWare 5+, Novell Storage Services (NSS)                                                                                                            |
| 70       | DiskSecure Multi-Boot                                                                                                                                       |
| 75       | IBM PC/IX                                                                                                                                                   |
| 80       | Minix v1.1 - 1.4a, Old MINIX (Linux)                                                                                                                        |
| 81       | Linux/Minix v1.4b+, Mitac Advanced Disk Manager                                                                                                             |
| 82       | Linux Swap partition, Prime or Solaris (Unix)                                                                                                               |
| 83       | Linux native file systems (ext2/3/4, JFS, Reiser, xiafs, and others)                                                                                        |
| 84       | OS/2 hiding type 04h partition, APM hibernation, used by Win98.                                                                                             |
| 86       | NT Stripe Set, Volume Set?                                                                                                                                  |
| 87       | NT Stripe Set, Volume Set?, HPFS FT mirrored partition                                                                                                      |
| 93       | Amoeba file system, Hidden Linux EXT2 partition (PowerQuest)                                                                                                |
| 94       | Amoeba bad block table                                                                                                                                      |
| 99       | Mylex EISA SCSI                                                                                                                                             |
| 9F       | BSDI                                                                                                                                                        |
| A0       | Phoenix NoteBios Power Management "Save to Disk", IBM hibernation                                                                                           |
| A1       | HP Volume Expansion (SpeedStor variant)                                                                                                                     |
| A5       | FreeBSD/386                                                                                                                                                 |
| A6       | OpenBSD, HP Volume Expansion (SpeedStor variant)                                                                                                            |
| A7       | NextStep Partition                                                                                                                                          |
| A9       | NetBSD                                                                                                                                                      |
| AA       | Olivetti DOS with FAT12                                                                                                                                     |
| B0       | Bootmanager BootStar by Star-Tools GmbH                                                                                                                     |
| B7       | BSDI file system or secondarily swap                                                                                                                        |
| B8       | BSDI swap partition or secondarily file system                                                                                                              |
| BE       | Solaris boot partition                                                                                                                                      |
| C0       | Novell DOS/OpenDOS/DR-OpenDOS/DR-DOS secured partition                                                                                                      |
| C1       | DR-DOS 6.0 LOGIN.EXE-secured 12-bit FAT partition                                                                                                           |
| C4       | DR-DOS 6.0 LOGIN.EXE-secured 16-bit FAT partition                                                                                                           |
| C6       | DR-DOS 6.0 LOGIN.EXE-secured Huge partition, or corrupted FAT16 volume/stripe set (Windows NT)                                                              |
| C7       | Syrinx, Cyrnix, HPFS FT disabled mirrored partition, or corrupted NTFS volume/stripe set                                                                    |
| CB       | DR-DOS secured FAT32                                                                                                                                       |
| CE       | DR-DOS secured FAT16X (LBA)                                                                                                                                 |
| D0       | Multiuser DOS secured (FAT12?)                                                                                                                              |
| D1       | Old Multiuser DOS secured FAT12                                                                                                                             |
| D4       | Old Multiuser DOS secured FAT16 (<= 32M)                                                                                                                    |
| DF       | BootIt EMBRM                                                                                                                                               |
| E1       | SpeedStor 12-bit FAT Extended partition, DOS access                                                                                                        |
| E4       | SpeedStor 16-bit FAT Extended partition                                                                                                                     |
| EB       | BeOS file system                                                                                                                                           |
| EE       | Indicates a GPT Protective MBR followed by a GPT/EFI Header.                                                                                                |
| EF       | EFI/UEFI System Partition (or ESP); defines a UEFI system partition                                                                                         |
| F2       | DOS 3.3+ secondary partition                                                                                                                                |
| F4       | SpeedStor                                                                                                                                                |
| F7       | Partitions which span multiple drives, Advanced UNIX                                                                                                                                     |
| FB       | VMware file system partition                                                                                                                                                                                                                                                                                              |
| FC       | VMware swap partition                                                                                                                                       |
| FD       | Linux raid partition                                                                                                                                              |
| FE       | LANstep                                                                                                                                                                                                                       |
| FF       | BBt assistant partition, Older XENIX or Novel Netware                                                                                                                                                 |

## 6. References

1. [The Starman](https://thestarman.pcministry.com/asm/mbr/PartTables.htm#mbr)
2. [Know IT Like Pro](https://knowitlikepro.com/understanding-master-boot-record-mbr/)
