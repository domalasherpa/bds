PRAGMA foreign_keys=OFF;--> statement-breakpoint
CREATE TABLE `__new_userImages` (
	`id` integer PRIMARY KEY NOT NULL,
	`userId` integer NOT NULL,
	`path` text NOT NULL,
	`detectedBird` text,
	`createdAt` text DEFAULT CURRENT_TIMESTAMP NOT NULL,
	`updatedAt` text DEFAULT CURRENT_TIMESTAMP NOT NULL,
	FOREIGN KEY (`userId`) REFERENCES `users`(`id`) ON UPDATE no action ON DELETE cascade
);
--> statement-breakpoint
INSERT INTO `__new_userImages`("id", "userId", "path", "detectedBird", "createdAt", "updatedAt") SELECT "id", "userId", "path", "detectedBird", "createdAt", "updatedAt" FROM `userImages`;--> statement-breakpoint
DROP TABLE `userImages`;--> statement-breakpoint
ALTER TABLE `__new_userImages` RENAME TO `userImages`;--> statement-breakpoint
PRAGMA foreign_keys=ON;--> statement-breakpoint
CREATE UNIQUE INDEX `userImages_path_unique` ON `userImages` (`path`);