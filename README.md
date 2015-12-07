# IPmayak

Tracks changes of the system's external IP address and writes each new change to a given CSV file.

---

## Usage

Probably the best way to use this program is as a cron job.

### Ubuntu

1. Clone the repository
1. CD into it
1. Copy the file someplace safe
1. Mark it executable

  ```sh
  sudo chmod +x /home/<user>/bin/ipmayak.py
  ```

1. Add it to cron, for example

  ```sh
  crontab -e
  ```

  ```cron
  @hourly /home/<user>/bin/ipmayak.py <path/to/file.csv>
  ```
