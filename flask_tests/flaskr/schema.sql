CREATE TABLE `entries` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `title` TEXT NOT NULL COLLATE 'latin1_bin',
    `text` TEXT NOT NULL COLLATE 'latin1_bin',
    PRIMARY KEY (`id`)
)
COLLATE='latin1_bin'
ENGINE=InnoDB
;

CREATE TABLE `login` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `username` TEXT NOT NULL COLLATE 'latin1_bin',
    `password` TEXT NOT NULL COLLATE 'latin1_bin',
    PRIMARY KEY (`id`)
)
COLLATE='latin1_bin'
ENGINE=InnoDB
;

