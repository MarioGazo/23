CREATE TABLE assets (
    id int PRIMARY KEY AUTO_INCREMENT,
    type char(255),
    title char(255),
    label char(255),
    url char(255)
);

INSERT INTO `assets` (`id`, `type`, `title`, `label`, `url`) VALUES ('1', 'photo', 'title', 'label', 'https://google.com');
